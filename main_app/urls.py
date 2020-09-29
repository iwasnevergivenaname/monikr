from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('about/', views.about, name='about'),
    path('artist/', views.artist_index, name='artist_index'),
    path('artist/<int:pk>/', views.page, name='page'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('profile/<username>/', views.profile, name='profile'),
    path('text_exhibit/<int:pk>/', views.text_exhibit, name='text_exhibit'),
    path('text_exhibit/create/', views.TextExhibitCreate.as_view(), name='text_exhibit_create'),
    path('text_exhibit/<int:pk>/update/', views.TextExhibitUpdate.as_view(), name='text_exhibit_update'),
    path('text_exhibit/<int:pk>/delete/', views.TextExhibitDelete.as_view(), name='text_exhibit_delete'),
    path('photo_exhibit/upload/', views.upload, name='upload'),
    path('photo_exhibit/<int:pk>/', views.photo_exhibit, name='photo_exhibit'),
    path('photo_exhibit/<int:pk>/delete/', views.PhotoExhibitDelete.as_view(), name='photo_exhibit_delete'),
    path('artist/<int:pk>/commission/<id>/update/', views.CommissionUpdate.as_view(), name='commission_update'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('tags/', views.tags_index, name='tags_index'),
    path('tags/<int:tag_id>', views.tags_show, name='tags_show'),
    path('tags/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    path('artist/<int:pk>/salon/', views.salon, name='salon'),
    path('artist/<int:pk>/salon/1/', views.salon_post, name='salon_post'),
]

#  profile url should be artist/:moniker

