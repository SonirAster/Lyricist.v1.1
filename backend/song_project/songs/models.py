from django.db import models

# Create your models here.


class Character(models.Model):
    char = models.CharField(max_length=1)

    def __str__(self):
        return self.char


class Language(models.Model):
    lang = models.CharField(max_length=55)

    def __str__(self):
        return self.lang


class Genre(models.Model):
    genre = models.CharField(max_length=150)

    def __str__(self):
        return self.genre


class Year(models.Model):
    year = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.year}'


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='groups/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    year = models.ForeignKey(Year, on_delete=models.PROTECT, null=True)
    language = models.ManyToManyField(Language,)
    character = models.ForeignKey(Character, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    year = models.ForeignKey(Year, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to='albums/')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, null=True)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    character = models.ForeignKey(Character, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
