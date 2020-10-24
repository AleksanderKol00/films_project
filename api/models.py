from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class Award(models.Model):
    name = models.CharField(max_length=255)


class Poster(models.Model):
    url = models.URLField()


class RatingSource(models.Model):
    name = models.CharField(max_length=255)


class Rating(models.Model):
    source = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class FilmType(models.Model):
    name = models.CharField(max_length=255)


class LegalPerson(models.Model):
    name = models.CharField(max_length=255)


class Website(models.Model):
    url = models.URLField()  # TODO check


class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    rated = models.CharField(max_length=255, blank=True)  # TODO check
    runtime_seconds = models.IntegerField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    directors = models.ManyToManyField(Person, blank=True)
    writers = models.ManyToManyField(Person, through="FilmWriter", related_name="writers")
    actors = models.ManyToManyField(Person, blank=True, related_name="actors")
    plot = models.TextField(blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    countries = models.ManyToManyField(Country, blank=True)
    awards = models.ManyToManyField(Award, blank=True)
    posters = models.ManyToManyField(Poster, blank=True)
    imdbID = models.CharField(max_length=255, blank=True)
    film_type = models.ForeignKey(
        FilmType, blank=True, null=True, on_delete=models.SET_NULL
    )
    dvd = models.CharField(max_length=255, blank=True)  # TODO check
    box_office = models.CharField(max_length=255, blank=True)  # TODO check
    production = models.ManyToManyField(LegalPerson, blank=True)
    website = models.ManyToManyField(Website, blank=True)


class FilmWriter(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    writer = models.ForeignKey(Person, on_delete=models.CASCADE)
    type_of_work = models.CharField(max_length=255)


# TODO add constraints
