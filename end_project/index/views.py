# views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required

@login_required  # Ceci assure que l'utilisateur doit être authentifié pour accéder à cette vue
def index(request):
    username = request.user.username  # Obtenez le nom d'utilisateur de l'utilisateur connecté
    return render(request, 'index.html', {'username': username})


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigez vers la page d'accueil après la connexion
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return redirect('index')