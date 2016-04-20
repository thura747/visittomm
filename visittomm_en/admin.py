from django.contrib import admin

# Register your models here.

from .models import Post2, Cities, RegionsStates

admin.site.register(Post2)

admin.site.register(Cities)
admin.site.register(RegionsStates)
