from django.shortcuts import render
from django.shortcuts import redirect
from pages.models import Gym
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    if request.method == 'GET':
        gyms = Gym.objects.all()
        return render(request, 'pages/index.html', {'gyms': gyms})


def review(request):
  return render(request, 'pages/review.html')


def new(request):
  return render(request, 'pages/new.html')

@ensure_csrf_cookie
def get_data(request):
    if request.method == 'POST':
        print(request.POST['people_num'])
