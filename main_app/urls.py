from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('artist/', views.artist_index, name='artist_index'),
    path('artist/<int:pk>/', views.page, name='page'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('profile/<username>/', views.profile, name='profile'),
    path('exhibit/<int:pk>/', views.exhibit, name='exhibit'),
    path('exhibit/create/', views.ExhibitCreate.as_view(), name='exhibit_create'),
    path('exhibit/<int:pk>/update/', views.ExhibitUpdate.as_view(), name='exhibit_update'),
    path('exhibit/<int:pk>/delete/', views.ExhibitDelete.as_view(), name='exhibit_delete'),
    path('exhibit/upload/', views.upload, name='upload')
]

#  profile url should be artist/:moniker

