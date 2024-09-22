from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/add-pet.html')


def pet_details(request, username, pet_slug):
    return render(request, 'pets/pet-details.html')


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/edit-pet.html')


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/delete-pet.html')
