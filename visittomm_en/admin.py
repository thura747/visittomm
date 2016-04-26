from django.contrib import admin

# Register your models here.

from .models import Post2

from .models import Cities, RegionsStates, Destinations, Packages, Companies

admin.site.register(Post2)

admin.site.register(Cities)
admin.site.register(RegionsStates)
admin.site.register(Destinations)
admin.site.register(Packages)
admin.site.register(Companies)
