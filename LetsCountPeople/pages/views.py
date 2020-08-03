from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from pages.models import Gym, CurrentPeople, Review
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    if request.method == 'GET':
        gyms = Gym.objects.all()
        return render(request, 'pages/index.html', {'gyms': gyms})


def review(request):
  reviews = Review.objects.all()
  return render(request, 'pages/review.html', {'reviews' : reviews})


def new(request):
<<<<<<< HEAD
  if request.method == "POST":
    gym = Gym.objects.get(id = 1)
    author = request.user
    title = request.POST['review-title']
    content = request.POST['review-content']
    Review.objects.create(gym = gym, author = author, title = title, content = content)
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
    return render(request, 'pages/show.html', {'review': review})
  return render(request, 'pages/update.html', {'review': review})


def delete(request, id):
  review = Review.objects.get(id = id)
  review.delete()
  return redirect('/pages/review/')


def search_result(request):
    gym_names = None
    query = None
    gym_all = Gym.objects.all()
    if 'q' in request.GET:
        query = request.GET.get('q')
        gym_names = gym_all.filter(
            Q(name__icontains=query) | Q(address__icontains=query))
    else:
        gym_names = gym_all
    return render(request, 'pages/index.html', {'query': query, 'gyms': gym_names})

@ensure_csrf_cookie
def get_data(request):
  if request.method =='POST':
    CurrentPeople.objects.create(num_people=request.POST['people_num'])
  return None
