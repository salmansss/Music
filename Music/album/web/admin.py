from django.contrib import admin
from .models import Album, Song, Login, Register

# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Login)
admin.site.register(Register)