import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_index_view():
    client = Client()
    url = reverse('index')  # Remplacez 'index' par le nom d'URL de la vue index
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_view():
    client = Client()
    url = reverse('login')  # Remplacez 'login_view' par le nom d'URL de la vue login_view
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_custom_logout_view():
    client = Client()
    url = reverse('logout')  # Remplacez par le nom d'URL de la vue custom_logout_view
    response = client.get(url)
    assert response.status_code == 302  # Le statut peut varier selon le comportement attendu de la vue

@pytest.mark.django_db
def test_register_view():
    client = Client()
    url = reverse('register')  # Remplacez 'register' par le nom d'URL de la vue register
    response = client.get(url)
    assert response.status_code == 200

