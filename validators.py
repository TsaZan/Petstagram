from django.core.exceptions import ValidationError


def pet_photo_max_size_validator(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError(f'Image size must be less than 5MB. Your file is {(value.size / 1024 / 1024):.0f}MB')