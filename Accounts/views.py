from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        context['error'] = False
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Meanings:search'))
        else:
            context['error'] = True
            print('error')
    return render(request, 'login.html', context)

def user_signup(request):

    user = request.user
    context = {}
    if user:
        context['error'] = 'User Already Logged In'
    else:
        password = request.POST['password']
        check = request.POST['password2']
        if password != check:
            context['error'] = 'Passwords Do Not Match'
            return render(request, 'signup.html', context)
        username = request.POST['username']
        user = User.objects.get(username=username) or None
        if user:
            context['error'] = 'Username already taken'
            return render(request, 'signup.html', context)
        email = request.POST['email']
        user = User.objects.get(email=email) or None
        if user:
            context['error'] = 'Username already taken'
            return render(request, 'signup.html', context)
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'signup.html')

def user_logout(request):
    user = request.user
    if user.is_active:
        logout(request)

    return HttpResponseRedirect(reverse('Meanings:search'))