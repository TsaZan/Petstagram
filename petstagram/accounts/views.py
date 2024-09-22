from django.shortcuts import render


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def profile(request, pk):
    return render(request, 'accounts/profile-details.html')


def edit_profile(request, pk):
    return render(request, 'accounts/edit-profile.html')


def delete_profile(request, pk):
    return render(request, 'accounts/delete-profile.html')
