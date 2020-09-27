from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Artist
from .models import Exhibit
from django.contrib.auth.models import User

# from .models import Piece

class ArtistCreate(CreateView):
  model = Artist
  fields = '__all__'
  success_url = '/artist'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/artist')

class ArtistUpdate(UpdateView):
  model = Artist
  fields = ['monikr', 'pronouns', 'medium', 'artist_statement', 'icon', 'bg_color']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/artist/' + str(self.object.pk))

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artist'
  
  
#   FIX SUCCESS URL
class ExhibitCreate(CreateView):
  model = Exhibit
  fields = '__all__'
  success_url = '/exhibit'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/exhibit')

class ExhibitUpdate(UpdateView):
  model = Exhibit
  fields = ['title', 'content', 'materials_used', 'for_sale']
  
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/exhibit/' + str(self.object.pk))
  
class ExhibitDelete(DeleteView):
  model = Exhibit
  success_url = '/exhibit'


# Create your views here.
def index(request):
  return render(request, 'index.html')


def about(request):
  return render(request, 'about.html')

def artist_index(request):
  artists = Artist.objects.all()
  return render(request, 'artists/index.html', {'artists': artists})

# these are returning all artist for one user, will change later but i just wanted to get auth up and running
def profile(request, username):
    user = User.objects.get(username=username)
    artists = Artist.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'artists': artists})


# # should change to artist/:monikr for url
def page(request, int):
  artist = Artist.objects.get(id=int)
  exhibit = Exhibit.objects.all()
  # artist = Artist.objects.get(monikr=monikr)
  # piece = Piece.objects.get(id=1)
  return render(request, 'artists/page.html', {'artist': artist, 'exhibit': exhibit})

def exhibit(request, int):
  artist = Artist.objects.get(id=int)
  exhibit = Exhibit.objects.get(id=int)
  return render(request, 'artists/exhibit.html', {'artist': artist, 'exhibit': exhibit})

#



# artists = [
# 	Artist('sleepy icarus', 'comfort in loneliness', 'vaporwave', 'she/her', 'digital photography'),
# 	Artist('kathryn mace-shanahan', 'quilting isn\'t boring', 'experimental', 'she/her', 'quilts'),
# 	Artist('tima', 'cute things', '90\'s kid', 'she/her', 'laser cutting'),
# 	Artist('tiza', 'i\'m a cool chick', 'lite goth', 'she/her', 'bending'),
# ]
