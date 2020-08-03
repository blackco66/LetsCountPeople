from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from pages.models import Gym


def index(request):
    gyms = Gym.objects.all()
    return render(request, 'pages/index.html', {'gyms': gyms})


def review(request):
    return render(request, 'pages/review.html')


def new(request):
    return render(request, 'pages/new.html')


def search_result(request):
    gym_names = None
    query = None
    gym_all = Gym.objects.all()
    if 'q' in request.GET:
        print('search')
        query = request.GET.get('q')
        gym_names = gym_all.filter(
            Q(name__contains=query) | Q(address__contains=query))
    else:
        print('nosearch')
        gym_names = gym_all
    return render(request, 'pages/index.html', {'query': query, 'gyms': gym_names})
