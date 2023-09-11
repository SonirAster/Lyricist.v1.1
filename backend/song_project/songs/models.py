from django.db import models

# Create your models here.


class Language(models.Model):
    lang = models.CharField(max_length=55)

    def __str__(self):
        return self.lang


class Genre(models.Model):
    genre = models.CharField(max_length=150)

    def __str__(self):
        return self.genre


class Group(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, null=True)
    year = models.SmallIntegerField(default=None)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    years = models.SmallIntegerField()
    image = models.ImageField(upload_to='media/')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    years = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(unique=True)


