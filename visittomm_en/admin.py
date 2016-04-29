from django.contrib import admin

from django_admin_bootstrapped.admin.models import SortableInline
# from grappelli.forms import GrappelliSortableHiddenMixin

# Register your models here.

from .models import Post2

from .models import Cities, RegionsStates, Destinations, Packages, Companies

admin.site.register(Post2)

admin.site.register(Cities)
# admin.site.register(RegionsStates)
admin.site.register(Destinations)
admin.site.register(Packages)
admin.site.register(Companies)

# class CitiesInline(GrappelliSortableHiddenMixin, admin.TabularInline):
class CitiesInline(admin.TabularInline, SortableInline):
    model = Cities
    # list_display = ["name", "city_code"]
    readonly_fields = ['name', 'city_code', 'postal_code', 'city']
    # fields = ['name']
    # extra = 1
    # fields = [ "name"]
    # exclude = ['name', 'city_code', 'postal_code', 'content', 'lat', 'lon', 'i_airport', 'd_airport',
    #            'bus', 'cruise', 'car', 'city', 'publish']
    exclude = ['content', 'lat', 'lon', 'i_airport', 'd_airport', 'bus', 'cruise', 'car', 'publish']
    show_change_link = True
    can_delete = True
    extra = 0


class RegonsStatesAdmin(admin.ModelAdmin):
    model = RegionsStates
    list_display = ["name", "code"]
    inlines = [
        CitiesInline,
    ]

admin.site.register(RegionsStates, RegonsStatesAdmin)



