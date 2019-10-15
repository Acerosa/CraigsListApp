from django.urls import path
from CraigslistApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('on_search', views.on_search, name='on_search'),
]