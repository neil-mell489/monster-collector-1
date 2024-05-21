from django.contrib import admin
from .models import Monster, Battle, Powerup, Photo


# Register your models here.

admin.site.register(Monster)
admin.site.register(Battle)
admin.site.register(Powerup)
admin.site.register(Photo)