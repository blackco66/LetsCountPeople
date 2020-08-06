from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from pages.models import Gym, CurrentPeople, Review, ReviewComment
from django.http import JsonResponse

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


def review(request):
  reviews = Review.objects.all()
  return render(request, 'pages/review.html', {'reviews': reviews})

def add_gym(request):
    name = request.POST['name']
    address = request.POST['address']
    if request.POST['latitude'] != '' and request.POST['longitude'] != '':
      latitude = request.POST['latitude']
      longitude = request.POST['longitude']
    else:
      latitude = None
      longitude = None
    new_gym = Gym.objects.create(name=name, address=address, latitude=latitude, longitude=longitude)

    return JsonResponse({"message": "created!"} , status=201)

def new(request):
  if request.method == "POST":
    gym = Gym.objects.get(id=1)
    author = request.user
    title = request.POST['review-title']
    content = request.POST['review-content']
    Review.objects.create(gym=gym, author=author, title=title, content=content)
    return redirect('/pages/review/')
  return render(request, 'pages/new.html')


def show(request, id):
  review = Review.objects.get(id = id)
  review.hits += 1
  review.save()
  return render(request, 'pages/show.html', {'review': review})


def update(request, id):
  review = Review.objects.get(id = id)
  if request.method == "POST":
    review.title = request.POST['review-title']
    review.content = request.POST['review-content']
    review.save()
    return redirect('/pages/review/'+str(id))
  return render(request, 'pages/update.html', {'review': review})


def delete(request, id):
  review = Review.objects.get(id=id)
  review.delete()
  return redirect('/pages/review/')


def comment(request, id):
  ReviewComment.objects.create(author=request.user, review_id=id, content=request.POST['content'])
  new_comment = ReviewComment.objects.latest('id')

  context = {
    'id': new_comment.id,
    'username': new_comment.author.username,
    'content': new_comment.content,
  }

  return JsonResponse(context)


# def comment_update(request, id, cid):
#   comment = ReviewComment.objects.get(id = cid)


def comment_delete(request, id, cid):
  review = Review.objects.get(id=id)
  comment = ReviewComment.objects.get(id=cid)
  comment.delete()
  return render(request, 'pages/show.html', {'review': review})


def get_data(request):
  if request.method =='POST':
    gym = Gym.objects.get(name=request.POST['gym_name'])
    CurrentPeople.objects.create(gym=gym,num_people=request.POST['people_num'])
  return redirect('/') 
