from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth
from .forms import UserLoginForm, UserRegistationForm, UserCreationForm


def index(request):
    return render(request, 'main/index.html')

def profile(request):
    return render(request, 'main/profil.html')
def index2(request):
    return render(request, 'main/index2.html')

def login(request):
    return render(request, 'main/login.html')

# def SignIn(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#             #return HttpResponseRedirect('')
#             return render(request, 'main/index2.html')
#     else:
#         form = UserLoginForm
#     context = {'form': form}
#     return render(request, 'main/signIn.html', context)
#
# def SignUp(request):
#     if request.method == 'POST':
#         form = UserRegistationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('signin'))
#         #return render(request, 'main/signIn.html')
#     else:
#         form = UserRegistationForm()
#     context = {'form': form}
#     return render(request, 'main/signUp.html', context)

def exit(request):
    logout(request)
    return render(request, 'main/index.html')

def login_or_register(request):
    form1 = UserLoginForm()
    form2 = UserRegistationForm()

    if request.method == 'POST':
        form1 = UserLoginForm(data=request.POST)
        if form1.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
            return render(request, 'main/index2.html')
    else:
        form1 = UserLoginForm()

    if request.method == 'POST':
        form2 = UserRegistationForm(data=request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('login_or_register'))
    context = {'form1': form1, 'form2': form2}
    return render(request, 'main/login.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, 'main/index.html')
#     else:
#         form = UserCreationForm
#     context = {'form': form}
#     return render(request, 'main/login.html', context)




