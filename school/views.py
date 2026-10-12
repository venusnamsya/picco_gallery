from django.shortcuts import render, redirect, get_object_or_400
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .models import Photo, Tag, Profile

def homepage(request):
    tag_filter = request.GET.get('tag')
    if tag_filter:
        photos = Photo.objects.filter(tags__name=tag_filter).distinct()
    else:
        photos = Photo.objects.all()
    
    tags = Tag.objects.all()
    return render(request, 'photo_gallery/homepage.html', {'photos': photos, 'tags': tags, 'selected_tag': tag_filter})

def photo_detail(request, pk):
    photo = get_object_or_400(Photo, pk=pk)
    return render(request, 'photo_gallery/photo_detail.html', {'photo': photo})

@login_required
def like_photo(request, pk):
    photo = get_object_or_400(Photo, pk=pk)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
        photo.dislikes.remove(request.user)
    return redirect('photo_detail', pk=pk)

@login_required
def dislike_photo(request, pk):
    photo = get_object_or_400(Photo, pk=pk)
    if request.user in photo.dislikes.all():
        photo.dislikes.remove(request.user)
    else:
        photo.dislikes.add(request.user)
        photo.likes.remove(request.user)
    return redirect('photo_detail', pk=pk)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'photo_gallery/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Simple inline bio update logic
        bio = request.POST.get('bio')
        request.user.profile.bio = bio
        request.user.profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    return render(request, 'photo_gallery/profile.html')
