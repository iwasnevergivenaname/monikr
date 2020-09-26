from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('artist/', views.artist_index, name='artist_index'),
    path('artist/<int>/', views.page, name='page'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('profile/<username>/', views.profile, name='profile')
]

#  profile url should be artist/:moniker

