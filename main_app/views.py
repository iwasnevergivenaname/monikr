from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Artist
from .models import Exhibit
from .models import Photo

from django.contrib.auth.models import User
import json

# import six
from cloudinary import api  # Only required for creating upload presets on the fly
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PhotoForm, PhotoDirectForm, PhotoUnsignedDirectForm
# from .models import Photo



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
	
# SEARCH PAGE AND RESULTS
class HomePageView(TemplateView):
	template_name = 'search.html'

class SearchResultsView(ListView):
	model = Artist
	template_name = 'search_results.html'
	
	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Artist.objects.filter(
			Q(monikr__icontains=query) | Q(artist_statement__icontains=query)
		)
		return object_list


# Create your views here.
def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def artist_index(request):
	artists = Artist.objects.all()
	return render(request, 'artists/index.html', {'artists': artists})

# def search(TemplateView):
# 	return render(request, 'search.html')


# these are returning all artist for one user, will change later but i just wanted to get auth up and running
def profile(request, username):
	user = User.objects.get(username=username)
	artists = Artist.objects.filter(user=user)
	return render(request, 'profile.html', {'username': username, 'artists': artists})


# # should change to artist/:monikr for url
def page(request, pk):
	artist = Artist.objects.get(pk=pk)
	exhibit = Exhibit.objects.filter(artist=artist)
	photo = Photo.objects.filter(artist=artist)
	return render(request, 'artists/page.html', {'artist': artist, 'exhibit': exhibit, 'photo': photo})


def exhibit(request, pk):
	artist = Artist.objects.get(pk=pk)
	exhibit = Exhibit.objects.get(pk=pk)
	# photo = Photo.objects.get(pk=pk)
	return render(request, 'artists/exhibit.html', {'artist': artist, 'exhibit': exhibit})


def photo(request, pk):
	# artist = Artist.objects.get(pk=pk)
	photo = Photo.objects.get(pk=pk)
	return render(request, 'artists/exhibit.html', {'photo': photo})


def upload(request):
	unsigned = request.GET.get("unsigned") == "true"
	
	if (unsigned):
		# For the sake of simplicity of the sample site, we generate the preset on the fly.
		# It only needs to be created once, in advance.
		try:
			api.upload_preset(PhotoUnsignedDirectForm.upload_preset_name)
		except api.NotFound:
			api.create_upload_preset(name=PhotoUnsignedDirectForm.upload_preset_name, unsigned=True, folder="preset_folder")
	
	direct_form = PhotoUnsignedDirectForm() if unsigned else PhotoDirectForm()
	context = dict(
		# Form demonstrating backend upload
		backend_form=PhotoForm(),
		# Form demonstrating direct upload
		direct_form=direct_form,
		# Should the upload form be unsigned
		unsigned=unsigned,
	)
	# When using direct upload - the following call is necessary to update the
	# form's callback url
	cl_init_js_callbacks(context['direct_form'], request)
	
	if request.method == 'POST':
		# Only backend upload should be posting here
		form = PhotoForm(request.POST, request.FILES)
		context['posted'] = form.instance
		if form.is_valid():
			# Uploads image and creates a model instance for it
			form.save()
	
	return render(request, 'upload.html', context)


def direct_upload_complete(request):
	form = PhotoDirectForm(request.POST)
	if form.is_valid():
		# Create a model instance for uploaded image using the provided data
		form.save()
		ret = dict(photo_id=form.instance.id)
	else:
		ret = dict(errors=form.errors)
	
	return HttpResponse(json.dumps(ret), content_type='application/json')
