from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Artist
# from .models import Piece

class ArtistCreate(CreateView):
  model = Artist
  fields = '__all__'
  success_url = '/artist'

class ArtistUpdate(UpdateView):
  model = Artist
  fields = ['moniker', 'pronouns', 'medium', 'artist_statement', 'icon']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/artist/' + str(self.object.pk))

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artist'

# Create your views here.
def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

def artist_index(request):
	artists = Artist.objects.all()
	return render(request, 'artists/index.html', {'artists': artists})

# should change to artist/:monikr for url
def profile(request):
	artist = Artist.objects.get(id=1)
	# piece = Piece.objects.get(id=1)
	return render(request, 'profile.html', {'artist': artist})

#



# artists = [
# 	Artist('sleepy icarus', 'comfort in loneliness', 'vaporwave', 'she/her', 'digital photography'),
# 	Artist('kathryn mace-shanahan', 'quilting isn\'t boring', 'experimental', 'she/her', 'quilts'),
# 	Artist('tima', 'cute things', '90\'s kid', 'she/her', 'laser cutting'),
# 	Artist('tiza', 'i\'m a cool chick', 'lite goth', 'she/her', 'bending'),
# ]
