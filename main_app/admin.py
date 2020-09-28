from django.contrib import admin
# import your models here
from .models import Artist
from .models import Contact
from .models import Commision
from .models import TextExhibit
from .models import PhotoExhibit
from .models import Tag


# Register your models here
admin.site.register(Artist)
admin.site.register(Commision)
admin.site.register(Contact)
admin.site.register(TextExhibit)
admin.site.register(PhotoExhibit)
admin.site.register(Tag)