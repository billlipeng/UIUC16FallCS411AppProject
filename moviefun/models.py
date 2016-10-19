from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    imdbrating = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    poster = models.CharField(max_length=500)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    runtime = models.CharField(max_length=200)
    rated = models.CharField(max_length=200)
    imdbid = models.CharField(max_length=200)

class Loc(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)

class MovieLocR(models.Model):
    loc_id = models.ForeignKey(Movie, related_name='loc_id', on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, related_name='movie_id', on_delete=models.CASCADE)

class RecomR(models.Model):
    movie1_id = models.ForeignKey(Movie, related_name='movie1_id', on_delete=models.CASCADE)
    movie2_id = models.ForeignKey(Movie, related_name='movie2_id', on_delete=models.CASCADE)

class TVPlay(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    season_number = models.CharField(max_length=200)
    episode_number = models.CharField(max_length=200)

# Create your models here.
