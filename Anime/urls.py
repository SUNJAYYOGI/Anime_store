from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anime/<int:anime_id>/', views.anime_detail, name='anime_detail'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
]

