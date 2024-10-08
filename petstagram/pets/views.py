from django.shortcuts import render, redirect

from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def add_pet(request):
    form = PetAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)
    context = {
        'form': form
    }
    return render(request, 'pets/add-pet.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    print(all_photos)

    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pets/pet-details.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {
        'form': form
    }
    return render(request, 'pets/edit-pet.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(instance=pet, initial=pet.__dict__)

    context = {
        'form': form}

    return render(request, 'pets/delete-pet.html', context)


def pet_posts(request):
    all_photos = Photo.objects.all()
    pets = Pet.objects.all()

    context = {
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-posts.html', context)
