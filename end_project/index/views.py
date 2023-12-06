# views.py
from django.contrib.auth import authenticate, login, logout, get_user
from django.shortcuts import render, redirect
from .forms import CustomLoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages  # Importez messages pour afficher des messages d'erreur
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=11f39b82-0464-4a30-8a0f-8315244325e5;IngestionEndpoint=https://francecentral-1.in.applicationinsights.azure.com/;LiveEndpoint=https://francecentral.livediagnostics.monitor.azure.com/'
))
#  # Assurez-vous d'importer votre CustomLoginForm
# from opencensus.ext.azure.log_exporter import AzureLogHandler
# import logging

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
                logger.info('Connexion réussie', extra={'custom_dimensions': {'username': username}})
                # logger.info('Connexion réussie', extra={'custom_dimensions': {'username': username}})
                return redirect('index')  # Redirigez vers la page d'accueil après la connexion
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Vérifiez si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d’utilisateur est déjà pris.')
            return redirect('register')

        # Créez l'utilisateur si le nom d'utilisateur est disponible
        user = User.objects.create_user(username=username, email=email, password=password)
        # Connectez l'utilisateur ou redirigez-le
        return redirect('index')  # Redirigez vers une page appropriée

    return render(request, 'register.html')
