from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name =models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    profile_picture = models.ImageField(upload_to='artist_images')


    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Album(models.Model):
    title = models.CharField(max_length=30, null=False)
    release_year = models.DateField()
    MUSIC_GENRES ={
        ("Rock", "Rock"),
        ("Música Clasica", "Música Clasica"),
        ("Cumbias", "cumbias"),
        ("Pop", "Pop"),
        ("Electrónica", "Electrónica")
    }
    genre = models.CharField(max_length=30, choices=MUSIC_GENRES, null=False) 
    associate_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    front_page = models.ImageField(upload_to='album_images')

    def __str__(self) -> str:
        return self.title
