from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
  if request.method == "POST":
    if request.POST['user-password'] == request.POST['user-password-check']:
      user = User.objects.create_user(username=request.POST['user-id'], password=request.POST['user-password'])
      user.backend = 'django.contrib.auth.backends.ModelBackend'
      auth.login(request, user)
      return redirect('/pages/')
  return render(request, 'accounts/signup.html')

# def login(request):
#   if request.method == "POST":
#     user = auth.authenticate(request, username = request.POST['user-id'], password = request.POST['user-password'])
#     if user is not None:
#       auth.login(request, user)
#       return redirect('/pages/')
#   return render(request, '/accounts/login.html')