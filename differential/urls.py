from django.urls import path, include
from . import views

app_name = 'differential'

urlpatterns = [
  path('', views.home, name='home'),
]
