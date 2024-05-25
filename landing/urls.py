from django.contrib import admin
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('activities', views.activities, name='activities'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
]
