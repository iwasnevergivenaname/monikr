from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def artist_index(request):
	return render(request, 'artists/index.html', {'artists': artists})


class Artist:
	def __init__(self, monikr, artist_statement, genre, pronouns, medium):
		self.monikr = monikr
		self.artist_statement = artist_statement
		self.genre = genre
		self.pronouns = pronouns
		self.medium = medium


artists = [
	Artist('sleepy icarus', 'comfort in loneliness', 'vaporwave', 'she/her', 'digital photography'),
	Artist('kathryn mace-shanahan', 'quilting isn\'t boring', 'experimental', 'she/her', 'quilts'),
	Artist('tima', 'cute things', '90\'s kid', 'she/her', 'laser cutting'),
	Artist('tiza', 'i\'m a cool chick', 'lite goth', 'she/her', 'bending'),
]
