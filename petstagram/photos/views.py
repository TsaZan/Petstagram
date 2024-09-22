from django.shortcuts import render


# Create your views here.
def add_photo(request):
    return render(request, 'photos/add-photo.html')


def photo_details(request, pk):
    return render(request, 'photos/photo-details.html')


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit.html')
