from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Artist
from .models import TextExhibit
from .models import PhotoExhibit
from .models import Tag
from django.contrib.auth.models import User
import json

# import six
from cloudinary import api  # Only required for creating upload presets on the fly
from cloudinary.forms import cl_init_js_callbacks
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PhotoForm, PhotoDirectForm, PhotoUnsignedDirectForm


# ARTIST CRUD
class ArtistCreate(CreateView):
	model = Artist
	fields = ['monikr', 'pronouns', 'medium', 'artist_statement', 'icon', 'bg_color']
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


@method_decorator(login_required, name='dispatch')
class ArtistDelete(DeleteView):
	model = Artist
	success_url = '/artist'


#   EXHIBIT CRUD
class TextExhibitCreate(CreateView):
	model = TextExhibit
	fields = ['title', 'content', 'materials_used', 'for_sale', 'tag']
	success_url = '/exhibit'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/exhibit')


class TextExhibitUpdate(UpdateView):
	model = TextExhibit
	fields = ['title', 'content', 'materials_used', 'for_sale', 'tags']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/exhibit/' + str(self.object.pk))


class TextExhibitDelete(DeleteView):
	model = TextExhibit
	success_url = '/artist'


class PhotoExhibitUpdate(UpdateView):
	model = TextExhibit
	fields = ['title', 'description', 'materials_used', 'for_sale', 'tags']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/exhibit/' + str(self.object.pk))


class PhotoExhibitDelete(DeleteView):
	model = PhotoExhibit
	success_url = '/artist'

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


# TAG CRUD
class TagCreate(CreateView):
	model = Tag
	fields = '__all__'
	success_url = '/tags'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/tags')


class TagUpdate(UpdateView):
	model = Tag
	fields = ['tag']
	success_url = '/tags'


class TagDelete(DeleteView):
	model = Tag
	success_url = '/tags'


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
	text_exhibit = TextExhibit.objects.filter(artist=artist)
	photo_exhibit = PhotoExhibit.objects.filter(artist=artist)
	return render(request, 'artists/page.html',
	              {'artist': artist, 'text_exhibit': text_exhibit, 'photo_exhibit': photo_exhibit})


def text_exhibit(request, pk):
	artist = Artist.objects.get(pk=pk)
	text_exhibit = TextExhibit.objects.get(pk=pk)
	# photo = Photo.objects.get(pk=pk)
	return render(request, 'artists/exhibit.html', {'artist': artist, 'text_exhibit': text_exhibit})


def photo_exhibit(request, pk):
	# artist = Artist.objects.get(pk=pk)
	photo_exhibit = PhotoExhibit.objects.get(pk=pk)
	return render(request, 'artists/exhibit.html', {'photo_exhibit': photo_exhibit})


# UPLOAD
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


#  TAGS
def tags_index(request):
	tags = Tag.objects.all()
	return render(request, 'tags/index.html', {'tags': tags})


def tags_show(request, tag_id):
	tag = Tag.objects.get(id=tag_id)
	return render(request, 'tags/show.html', {'tag': tag})


#  salon
def salon(request, pk):
	# salon = Salon.objects.get(pk=pk)
	return render(request, 'salon/salon.html')


def salon_post(request, pk):
	return render(request, 'salon/salon_post.html')


# AUTH
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return render(request, 'index.html', user)
	else:
		form = UserCreationForm()
		return render(request, 'auth/signup.html', {'form': form})


def login(request):
	context = {"error": False}
	if request.method == "GET":
		return render(request, 'auth/login.html')
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return render(request, 'index.html')


def logout(request):
	auth.logout(request)
	return render(request, 'index.html')
