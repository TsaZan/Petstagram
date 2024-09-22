from django.contrib import admin
from django.utils.safestring import mark_safe

from petstagram import settings
from petstagram.photos.models import Photo
from petstagram.settings import MEDIA_URL, MEDIA_ROOT


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_photo', 'description', 'tagged_pets', 'created_at')

    @staticmethod
    def show_photo(obj):
        return mark_safe(f'<img src="{MEDIA_URL}{obj.photo}" width="96" height="96" />')

    @staticmethod
    def tagged_pets(obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])
