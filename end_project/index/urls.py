from django.urls import path
from . import views
from .views import login_view, custom_logout_view,register

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', register, name='register'),
]


