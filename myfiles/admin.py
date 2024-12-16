from django.contrib import admin
from django.utils.safestring import mark_safe

from myfiles.models import Brands,Cars

# Register your models here.

admin.site.register(Brands)

class CarsAdmin(admin.ModelAdmin):
    list_display = ('id','name','enrolled_at','email','brand','get_photo')
    list_editable = ('brand',)
    list_filter = ('brand',)
    search_fields = ('name', 'brand')
    list_per_page = 10
    list_display_links = ('id', 'name','enrolled_at')

    def get_photo(self, i):
        if i.photo:
            return mark_safe(f'<img src="{i.photo.url}" width="150px">')
        return "-"

    get_photo.short_description = "Rasmi"

admin.site.register(Cars,CarsAdmin)