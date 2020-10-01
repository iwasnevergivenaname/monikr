from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from itertools import chain
from .models import Artist
from .models import TextExhibit
from .models import PhotoExhibit
from .models import Tag
from .models import Contact
from .models import Commission
from .models import Salon
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
	fields = ['title', 'content', 'materials_used', 'for_sale', 'tags']
	success_url = '/exhibit'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/text_exhibit')


class TextExhibitUpdate(UpdateView):
	model = TextExhibit
	fields = ['title', 'content', 'materials_used', 'for_sale', 'tags']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/text_exhibit/' + str(self.object.pk))


class TextExhibitDelete(DeleteView):
	model = TextExhibit
	success_url = '/artist'


class PhotoExhibitUpdate(UpdateView):
	model = PhotoExhibit
	fields = ['title', 'description', 'materials_used', 'for_sale', 'tags']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/photo_exhibit/' + str(self.object.pk))


class PhotoExhibitDelete(DeleteView):
	model = PhotoExhibit
	success_url = '/artist'


# COMMISSION CRUD
class CommissionCreate(CreateView):
	model = Commission
	fields = ['isOpened', 'disclaimer']
	success_url = '/artist'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/artist' + str(self.object.pk))


class CommissionUpdate(UpdateView):
	model = Commission
	fields = ['isOpened', 'disclaimer']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/artist/' + str(self.object.pk))


class CommissionDelete(DeleteView):
	model = Commission
	success_url = '/artist'


# CONTACT CRUD
class ContactCreate(CreateView):
	model = Contact
	fields = ['phone_number', 'website', 'store', 'instagram', 'facebook', 'twitter', 'etsy', 'other']
	success_url = '/artist'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect('/artist' + str(self.object.pk))


class ContactUpdate(UpdateView):
	model = Contact
	fields = ['phone_number', 'website', 'store', 'instagram', 'facebook', 'twitter', 'etsy', 'other']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/artist/' + str(self.object.pk))


class ContactDelete(DeleteView):
	model = Commission
	success_url = '/artist'


# SEARCH PAGE AND RESULTS
class HomePageView(TemplateView):
	template_name = 'search.html'



class SearchResultsView(ListView):
	model = Artist, Tag
	template_name = 'search_results.html'
	
	def get_queryset(self):
		query = self.request.GET.get('q')
		tag = Tag.objects.filter(Q(tag__icontains=query))
		artist = Artist.objects.filter(
			Q(monikr__icontains=query) | Q(artist_statement__icontains=query)
		).select_related()
		object_list = chain(tag, artist)
		print(object_list)
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


# Salon CRUD
class SalonCreate(CreateView):
	model = Salon
	fields = ['artist', 'title', 'content']
	success_url = '/salon'
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return HttpResponseRedirect('../' + str(self.object.pk))


class SalonUpdate(UpdateView):
	model = Salon
	fields = ['artist', 'author', 'title', 'content']
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect('/salon/' + str(self.object.pk))


class SalonDelete(DeleteView):
	model = Salon
	success_url = '/salon'


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
	user = User.objects.filter(artist=artist)
	try:
		currentUser = User.objects.get(username=request.user.username)
	except Exception as e:
		print(f'page error {e}')
		currentUser = None
	text_exhibit = TextExhibit.objects.filter(artist=artist)
	photo_exhibit = PhotoExhibit.objects.filter(artist=artist)
	contact = Contact.objects.filter(artist=artist)
	commission = Commission.objects.filter(artist=artist)
	return render(request, 'artists/page.html',
	              {'artist': artist, 'text_exhibit': text_exhibit, 'photo_exhibit': photo_exhibit,
	               'contact': contact, 'commission': commission, 'user': user, 'currentUser': currentUser})


def text_exhibit(request, pk):
	text_exhibit = TextExhibit.objects.get(pk=pk)
	artist = Artist.objects.filter(textexhibit=text_exhibit)
	user = User.objects.filter(artist=artist[0])
	tags = Tag.objects.filter(textexhibit=text_exhibit)
	try:
		currentUser = User.objects.get(username=request.user.username)
	except Exception as e:
		print(f"text exhibit error {e}")
		currentUser = None
	return render(request, 'artists/exhibit.html', {'text_exhibit': text_exhibit, 'artist': artist, 'currentUser': currentUser, 'tags': tags})


def photo_exhibit(request, pk):
	photo_exhibit = PhotoExhibit.objects.get(pk=pk)
	artist = Artist.objects.filter(photoexhibit=photo_exhibit)
	user = User.objects.filter(artist=artist[0])
	tags = Tag.objects.filter(photoexhibit=photo_exhibit)
	try:
		currentUser = User.objects.get(username=request.user.username)
	except Exception as e:
		print(f"photo exhibit error {e}")
		currentUser = None
	return render(request, 'artists/exhibit.html', {'photo_exhibit': photo_exhibit, 'artist': artist, 'currentUser': currentUser, 'tags': tags})


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


def tags_show(request, id):
	tag = Tag.objects.get(id=id)
	photo_exhibit = PhotoExhibit.objects.filter(tags=tag)
	text_exhibit = TextExhibit.objects.filter(tags=tag)
	return render(request, 'tags/show.html', {'tags': tag, 'id': id, 'photo_exhibit': photo_exhibit, 'text_exhibit': text_exhibit})


#  salon
def salon(request, pk):
	try:
		artist = Artist.objects.get(pk=pk)
		salon = Salon.objects.filter(artist=artist)
	except Exception as e:
		print(f"salon error {e}")
		artist = Artist.objects.get(pk=pk)
		salon = None
	return render(request, 'salon/salon.html', {'artist': artist, 'salon': salon})


def salon_post(request, pk, id):
	artist = Artist.objects.get(pk=pk)
	salon = Salon.objects.get(id=id)
	return render(request, 'salon/salon_post.html', {'artist': artist, 'salon': salon})


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


def login_view(request):
	# if post, then authenticate (user submitted username and password)
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username=u, password=p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print('The account has been disabled.')
			else:
				print('The username and/or password is incorrect.')
	else:  # it was a get request so send the emtpy login form
		form = AuthenticationForm()
		return render(request, 'auth/login.html', {'form': form})


def logout(request):
	auth.logout(request)
	return render(request, 'index.html')
