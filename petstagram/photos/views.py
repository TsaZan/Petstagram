from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    form = PhotoAddForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'photos/add-photo.html', context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    like = photo.like_set.all()
    count = photo.like_set.count()
    comments = photo.comment_set.all()
    form = CommentForm()

    context = {
        'photo': photo,
        'like': like,
        'count': count,
        'comments': comments,
        'comment_form': form,
    }

    return render(request, 'photos/photo-details.html', context)


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {'form': form}

    return render(request, 'photos/photo-edit.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return render(request, 'accounts/profile-details.html')
