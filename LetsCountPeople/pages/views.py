from django.shortcuts import render
from django.shortcuts import redirect
from pages.models import Gym, CurrentPeople, Review

def index(request):
    gyms = Gym.objects.all()
    return render(request, 'pages/index.html', {'gyms': gyms})


def review(request):
  reviews = Review.objects.all()
  return render(request, 'pages/review.html', {'reviews' : reviews})


def new(request):
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