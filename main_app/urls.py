from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout, name="logout"),
    path('about/', views.about, name='about'),
    path('artist/', views.artist_index, name='artist_index'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/', views.page, name='page'),
    path('icon/upload/', views.icon_upload, name='icon_upload'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('profile/<username>/', views.profile, name='profile'),
    path('text_exhibit/<int:pk>/', views.text_exhibit, name='text_exhibit'),
    path('text_exhibit/create/', views.TextExhibitCreate.as_view(), name='text_exhibit_create'),
    path('text_exhibit/<int:pk>/update/', views.TextExhibitUpdate.as_view(), name='text_exhibit_update'),
    path('text_exhibit/<int:pk>/delete/', views.TextExhibitDelete.as_view(), name='text_exhibit_delete'),
    path('photo_exhibit/upload/', views.upload, name='upload'),
    path('photo_exhibit/<int:pk>/', views.photo_exhibit, name='photo_exhibit'),
    path('photo_exhibit/<int:pk>/update/', views.PhotoExhibitUpdate.as_view(), name='photo_exhibit_update'),
    path('photo_exhibit/<int:pk>/delete/', views.PhotoExhibitDelete.as_view(), name='photo_exhibit_delete'),
    path('artist/<int:pk>/commission/<id>/update/', views.CommissionUpdate.as_view(), name='commission_update'),
    path('artist/<int:pk>/contact/<id>/update/', views.ContactUpdate.as_view(), name='contact_update'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('tags/', views.tags_index, name='tags_index'),
    path('tag/<id>/', views.tags_show, name='tags_show'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    path('tag/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    path('artist/<int:pk>/salon/', views.salon, name='salon'),
    path('artist/<int:pk>/salon/create/', views.SalonCreate.as_view(), name='salon_create'),
    path('artist/<int:pk>/salon/<id>/', views.salon_post, name='salon_post'),
    re_path(r'^(?P<path>.*)/$',views.error404),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  profile url should be artist/:moniker

