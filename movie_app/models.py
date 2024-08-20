from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_url(self):
        return reverse('one-director', args=[self.id])

class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.floor} {self.number}"

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Дама'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    # slug = models.SlugField(default='', null=False)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.first_name)
    #     super(Actor, self).save(*args, **kwargs)

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актёр {self.first_name} {self.last_name}"
        else:
            return f"Актриса {self.first_name} {self.last_name}"

    def get_url(self):
        return reverse('one-actor', args=[self.id])

class Movie(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')  # по умолчанию related_name='movie_set'
    actors = models.ManyToManyField(Actor)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-movie', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"


# python manage.py shell_plus --print-sql
# from movie_app.models import Movie
