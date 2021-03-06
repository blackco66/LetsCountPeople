from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
  if request.method == "POST":
    if request.POST['user-password'] == request.POST['user-password-check']:
      user = User.objects.create_user(username=request.POST['user-id'], password=request.POST['user-password'])
      auth.login(request, user)
      return redirect('/pages/')
  return render(request, 'accounts/signup.html')

def login(request):
  redirect_to = request.GET.get('next', '/pages/')
  if request.method == "POST":
    user = auth.authenticate(request, username = request.POST['login-username'], password = request.POST['password'])
    if user is not None:
      auth.login(request, user)
      return redirect(redirect_to)
  return render(request, 'accounts/login.html', {'redirect_to': redirect_to})
