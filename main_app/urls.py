from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('artists/', views.artist_index, name='artist_index'),
    path('profile/', views.profile, name='profile')
]

#  profile url should be artist/:moniker

