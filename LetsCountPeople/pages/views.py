from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from pages.models import Gym, CurrentPeople, Review, ReviewComment
from pages.models import ReviewRec, CommentRec
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import ListView


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


def reviews(request):
  review_list = Review.objects.order_by('-created_at')
  paginator = Paginator(review_list, 10)
  review = request.GET.get('review')
  reviews = paginator.get_page(review)
  return render(request, 'pages/review.html', {'reviews': reviews})


class ReviewListView(ListView):
  model = Review
  template_name = "pages/review.html"
  context_object_name = 'reviews'
  paginate_by = 10

  def get_context_data(self, **kwargs):
    context = super(ReviewListView, self).get_context_data(**kwargs)
    paginator = context['paginator']
    page_numbers_range = 10
    max_index = len(paginator.page_range)

    page = self.request.GET.get('page')
    current_page = int(page) if page else 1

    start_index = int((current_page - 1) / page_numbers_range ) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
      end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    context['page_range'] = page_range
    return context


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