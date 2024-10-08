from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from validators import pet_photo_max_size_validator


class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=[pet_photo_max_size_validator, ])
    description = models.CharField(max_length=300,
                                   validators=[MinLengthValidator(10), ],
                                   blank=True,
                                   null=True)

    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(to=Pet, blank=True)
    created_at = models.DateTimeField(auto_now=True)

