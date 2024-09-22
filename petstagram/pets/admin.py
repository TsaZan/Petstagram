from django.contrib import admin
from django.utils.html import format_html

from petstagram.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date_of_birth', 'show_pet_image')

    @admin.display(description="Pet image")
    def show_pet_image(self, obj):
        return format_html("<a href='{url}'><img src='{url}' width='96'/></a>", url=obj.personal_photo)
