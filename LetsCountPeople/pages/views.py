from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from pages.models import Gym, CurrentPeople, Review, ReviewComment
from pages.models import ReviewRec, CommentRec
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def index(request):
  if request.method == 'GET':
    gyms = Gym.objects.all()
    return render(request, 'pages/index.html', {'gyms': gyms})


def search_result(request):
  gym_names = None
  query = None
  gym_all = Gym.objects.all()
  if 'q' in request.POST:
    query = request.POST.get('q')
    gym_names = gym_all.filter(
      Q(name__icontains=query) | Q(address__icontains=query))
  else:
    gym_names = gym_all
  return render(request, 'pages/index.html', {'query': query, 'gyms': gym_names})


def review_list(request):
  error = ""
  if request.method == "POST":
    search_v = request.POST['search-value']
    review_all = Review.objects.all().order_by('-id')

    if request.POST['search-type'] == "title":
      reviews = review_all.filter(title__icontains=search_v)
    elif request.POST['search-type'] == "content":
      reviews = review_all.filter(content__icontains=search_v)
    elif request.POST['search-type'] == "author":
      author = User.objects.all().get(username__icontains=search_v).id
      reviews = review_all.filter(author_id=author)
    elif request.POST['search-type'] == "gym":
      gym = Gym.objects.all().get(name__icontains=search_v).id
      reviews = review_all.filter(gym_id=gym)
    elif request.POST['search-type'] == "title-content":
      reviews = review_all.filter(
        Q(title__icontains=search_v) | Q(content__icontains=search_v))

    if reviews.count() == 0:
      error = "조건을 만족하는 게시글이 없습니다!"
  else:
    reviews = Review.objects.order_by('-id')

  page = int(request.GET.get('page', '1'))
  paginator = Paginator(reviews, 10)
  review_page = paginator.page(page)

  page_num = 10
  start_index = 1

  for i in reversed(range(1, page + 1)):
    if i % page_num == 1:
      start_index = i
      break;

  end_index = start_index + page_num
  if end_index > paginator.num_pages:
    end_index = paginator.num_pages + 1

  page_range = range(start_index, end_index)
  current = page
  return render(request, 'pages/review.html',
                {'reviews': review_page, 'page_range': page_range, 'current': current, 'error': error})


def add_gym(request):
  name = request.POST['name']
  address = request.POST['address']
  if request.POST['latitude'] != '' and request.POST['longitude'] != '':
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
  else:
    latitude = None
    longitude = None
  new_gym = Gym.objects.create(
    name=name, address=address, latitude=latitude, longitude=longitude)
  return JsonResponse({"message": "created!"}, status=201)


def new(request): 
  if request.method == "POST":
    name = request.POST['gym']
    gym = Gym.objects.get(name=name)
    author = request.user
    title = request.POST['review-title']
    content = request.POST['review-content']
    Review.objects.create(gym=gym, author=author, title=title, content=content)
    return redirect('/pages/review/')
  gyms = Gym.objects.all()
  return render(request, 'pages/new.html', {'gyms': gyms})


def show(request, id):
  review = Review.objects.get(id=id)
  review.hits += 1
  review.save()
  return render(request, 'pages/show.html', {'review': review})


def edit(request, id):
  review = Review.objects.get(id=id)
  if request.method == "POST":
    review.title = request.POST['review-title']
    review.content = request.POST['review-content']
    review.save()
    return redirect('/pages/review/'+str(id))
  return render(request, 'pages/edit.html', {'review': review})


def delete(request, id):
  review = Review.objects.get(id=id)
  review.delete()
  return redirect('/pages/review/')


def comment(request, id):
  new_comment = ReviewComment.objects.create(author=request.user, review_id=id, content=request.POST['content'])
  
  context = {
    'id': new_comment.id,
    'username': new_comment.author.username,
    'content': new_comment.content,
  }
  return JsonResponse(context)


def comment_delete(request, id, cid):
  review = Review.objects.get(id=id)
  comment = ReviewComment.objects.get(id=cid)
  comment.delete()
  return JsonResponse({'message' : 'deleted!'})


def get_data(request):
  if request.method == 'POST':
    gym = Gym.objects.get(name=request.POST['gym_name'])
    CurrentPeople.objects.create(
      gym=gym, num_people=request.POST['people_num'])
  return redirect('/')


def review_recommend(request, id):
  review = Review.objects.get(id=id)
  user = request.user 
  rec_already = ReviewRec.objects.filter(user = user, review = review)

  if rec_already:
    rec_already.delete()
  else:
    ReviewRec.objects.create(user = user, review = review)
  
  return redirect('/pages/review/'+str(id))


def comment_recommend(request, id, cid):
  comment = ReviewComment.objects.get(id=cid)
  user = request.user
  rec_already = CommentRec.objects.filter(user_id = user.id, comment_id = cid)

  if rec_already:
    rec_already.delete()
  else:
    CommentRec.objects.create(user=user, comment=comment)

  return redirect('/pages/review/'+str(id))
