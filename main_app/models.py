from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=True)
    # photo_exhibits = models.ManyToManyField(PhotoExhibit)
    # text_exhibits = models.ManyToManyField(TextExhibit)

    def __str__(self):
        return self.tag

class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monikr = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50, blank=True)
    medium = models.CharField(max_length=50)
    artist_statement = models.CharField(max_length=250)
    icon =  models.CharField(max_length=250, default='upload icon')
    bg_color = models.CharField(max_length=50, default='white')
 
    # icon =
    # category =
    # location =
    # press =
    # subject =
    # tags =
    # associated_artist
    
    def __str__(self):
        return self.monikr

    
class Contact(models.Model):
    artist = models.OneToOneField(
        Artist,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # email = User.email
    phone_number = models.IntegerField(default=None, blank=True)
    website = models.CharField(max_length=50, blank=True)
    store = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    etsy = models.CharField(max_length=50, blank=True)
    other = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.website
    
    
class Commission(models.Model):
    artist = models.OneToOneField(
        Artist,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    isOpened = models.BooleanField(default=False)
    disclaimer = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.disclaimer
    

class TextExhibit(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='title')
    content = models.TextField(max_length=1000, default='write it out here')
    materials_used = models.CharField(max_length=100, default='materials')
    for_sale = models.BooleanField(blank=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class PhotoExhibit(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    ## Misc Django Fields
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)
    description = models.CharField(max_length=100, default='write it out here')
    materials_used = models.CharField(max_length=100, default='materials')
    tags = models.ManyToManyField(Tag)

    ## Points to a Cloudinary image
    image = CloudinaryField('image')

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
    
# class SalonPost(models.Model):

class Observer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class Salon(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='title')
    content = models.TextField(max_length=1000, default='write it out here')
    
class Remebered(models.Model):
    observer = models.ForeignKey(Observer, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)