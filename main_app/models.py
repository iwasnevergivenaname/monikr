from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tag

class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monikr = models.CharField(max_length=100)
    # style = (
    #     ('')
    # )
    pronouns = models.CharField(max_length=50)
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
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # email = User.email
    phone = models.IntegerField(default=None)
    website = models.CharField(max_length=50, default=None)
    store = models.CharField(max_length=50, default=None)
    instagram = models.CharField(max_length=50, default=None)
    facebook = models.CharField(max_length=50, default=None)
    twitter = models.CharField(max_length=50, default=None)
    etsy = models.CharField(max_length=50, default=None)
    other = models.CharField(max_length=50, default=None)
    
    
class Commision(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    isOpened = models.BooleanField(default=False)
    dislcaimer = models.CharField(max_length=250, default=None)
    

class Exhibit(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='title')
    content = models.CharField(max_length=100, default='write it out here')
    materials_used = models.CharField(max_length=100, default='materials')
    for_sale = models.BooleanField(blank=False)


class Photo(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    ## Misc Django Fields
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)
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
    
