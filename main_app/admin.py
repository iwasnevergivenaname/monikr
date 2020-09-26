from django.contrib import admin
# import your models here
from .models import Artist
# from .models import Piece
from .models import Contact
from .models import Commision


# Register your models here
admin.site.register(Artist)
# admin.site.register(Piece)
admin.site.register(Commision)
admin.site.register(Contact)