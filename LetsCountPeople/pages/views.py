from django.shortcuts import render
from django.shortcuts import redirect
from pages.models import Gym

def index(request):
    gyms = Gym.objects.all()
    return render(request, 'pages/index.html', {'gyms': gyms})
