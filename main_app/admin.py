from django.contrib import admin
# import your models here
from .models import Artist
from .models import Contact
from .models import Commission
from .models import TextExhibit
from .models import PhotoExhibit
from .models import Tag
from .models import Observer
from .models import Salon
from .models import Remebered


# Register your models here
admin.site.register(Artist)
admin.site.register(Commission)
admin.site.register(Contact)
admin.site.register(TextExhibit)
admin.site.register(PhotoExhibit)
admin.site.register(Tag)
admin.site.register(Observer)
admin.site.register(Salon)
admin.site.register(Remebered)