from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    monikr = models.CharField(max_length=100)
    # style = (
    #     ('')
    # )
    pronouns = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    artist_statement = models.CharField(max_length=250)
    icon =  models.CharField(max_length=250, default='upload icon')
    # icon =
    # category =
    # location =
    # press =
    # subject =
    # tags =
    # associated_artist
    
    def __str__(self):
        return self.monikr


# class Piece(models.Model):
#     # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     title = models.CharField(max_length=50, default=None)
#     media = models.CharField(max_length=100, default=None)
#     description = models.CharField(max_length=250, default=None)
#     materials_used = models.CharField(max_length=100, default=None)
#     for_sale = models.BooleanField(default=False, blank=False)
#     price = models.FloatField(default=None)
#     tw = models.BooleanField(default=False, blank=False)
#
    
class Contact(models.Model):
    # artist_is
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
    # artist_id
    isOpened = models.BooleanField(default=False)
    dislcaimer = models.CharField(max_length=250, default=None)

