from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
from .models import Piece


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
	pieces = Piece.objects.get(id=5)
	return render(request, 'profile.html', {'artist': artist, 'pieces': pieces})

#



# artists = [
# 	Artist('sleepy icarus', 'comfort in loneliness', 'vaporwave', 'she/her', 'digital photography'),
# 	Artist('kathryn mace-shanahan', 'quilting isn\'t boring', 'experimental', 'she/her', 'quilts'),
# 	Artist('tima', 'cute things', '90\'s kid', 'she/her', 'laser cutting'),
# 	Artist('tiza', 'i\'m a cool chick', 'lite goth', 'she/her', 'bending'),
# ]
