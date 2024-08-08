from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields ='__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'},),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'},),
            'country' : forms.TextInput(attrs={'class' : 'form-control'},),
            'profile_picture':forms.ClearableFileInput(attrs={'class' : 'form-control'}),

        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields ='__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class' : 'form-control'}),
            'release_year': forms.DateInput(attrs={'class' : 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'associate_artist':forms.Select(attrs={'class': 'form-control'}),
            'front_page':forms.ClearableFileInput(attrs={'class' : 'form-control'}),
        }
