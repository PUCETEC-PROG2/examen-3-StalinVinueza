# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth import logout as auth_logout

from .models import Artist, Album
from .forms import ArtistForm, AlbumForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    artist = Artist.objects.order_by('country') 
    albums = Album.objects.order_by('genre')
    template = loader.get_template('index.html')
    return render (request, 'index.html', {'artist':artist, 'albums':albums})

def artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def album(request, album_id):
    
    album = Album.objects.get(id=album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm()
    
    return render(request, 'artist_form.html', {'form': form})

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk = id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm(instance=artist)
    
    return render(request, 'artist_form.html', {'form': form})

@login_required
def edit_album(request, id):
    album = get_object_or_404(Album, pk = id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect(':album_managerindex')
    else:
        form = AlbumForm(instance=album)
    
    return render(request, 'album_form.html', {'form': form})

@login_required
def delete_artist(required, id):
    artist = get_object_or_404(Artist, pk = id)
    artist.delete()
    return redirect('album_manager:index')

@login_required
def delete_album(required, id):
    album = get_object_or_404(Album, pk = id)
    album.delete()
    return redirect('album_manager:index')


def logout(request):
    auth_logout(request)
    return redirect('album_manager:index')


class CustomLoginView(LoginView):
    template_name = 'login.html'

