from django import forms
from django.forms import ModelForm

from petstagram.pets.models import Pet


class PetBaseModelForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class PetAddForm(PetBaseModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'personal_photo', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link To Image'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),

        }

        labels = {
            'name': 'Name:',
            'personal_photo': 'Personal Photo:',
            'date_of_birth': 'Date Of Birth:',
        }


class PetEditForm(PetBaseModelForm):
    pass


class PetDeleteForm(PetBaseModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'personal_photo', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'disabled': 'disabled'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Link To Image'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),

        }

