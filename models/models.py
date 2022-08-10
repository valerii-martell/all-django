from django.db import models
from datetime import datetime, timedelta

from django.contrib.auth.models import User

# # Create your models here.


class Example(models.Model):
    integer_field           = models.IntegerField()
    positive_field          = models.PositiveIntegerField()
    positive_small_field    = models.PositiveSmallIntegerField()
    big_integer_field       = models.BigIntegerField()
    float_field             = models.FloatField()
    binary_field            = models.BinaryField()
    boolean_field           = models.BooleanField()
    char_field              = models.CharField(max_length=5)
    text_field              = models.TextField(max_length=20)
    date_field              = models.DateField(auto_now = False)
    date_time_field         = models.DateTimeField(auto_now_add=False)
    decimal_field           = models.DecimalField(max_digits = 8, decimal_places = 2) #222222.22
    email                   = models.EmailField()
    file_field              = models.FileField(upload_to = 'file')
    image_field             = models.ImageField(upload_to = 'images')


class Author(models.Model):
    name        = models.CharField(max_length=50 , verbose_name = "Имя")
    surname     = models.CharField(max_length=50 , verbose_name = "Фамилия")
    date_birth  = models.DateField(auto_now=False , verbose_name = "Дата рождения")

    def __str__(self):
        return "Имя : %s Фамилия : %s" %(self.name, self.surname)


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    CHOISE_GENRE = (
        ('comedy' , "Comedy"),
        ('tragedy' , "Tragedy"),
        ('drama' , "Drama"),
    )

    author  = models.ForeignKey(Author , on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    text    = models.TextField(max_length=1000)
    genre   = models.CharField(max_length=50 ,choices=CHOISE_GENRE)


    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete = models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)




class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title', )



class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline', )


class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(null=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True,
                                        null=True)
    could_use_in_bouquet = models.BooleanField(default=True, null=True)
    wiki_page = models.URLField(default="https://www.wikipedia.org/",
                                name="wikipedia",
                                unique_for_date="delivered_at", null=True)
    name = models.CharField(max_length=64, unique=True, null=True)


class Bouquet(models.Model):
    shop = models.Manager()
    fresh_period = models.DurationField(default=timedelta(days=5), null=True,
                                        help_text="Use this field when you need"
                                                  " to have information about "
                                                  "bouquet fresh time")
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0, null=True)
    flowers = models.ManyToManyField(Flower,
                                     verbose_name="This bouquet"
                                                  " consists of this flowers")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    second_email = models.EmailField(null=True)
    name = models.CharField(max_length=64, null=True)
    invoice = models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')
    user_uuid = models.UUIDField(editable=False, null=True)
    discount_size = models.DecimalField(max_digits=5, decimal_places=5,
                                        null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True,
                                             protocol="IPv4")

    def __str__(self):
        return self.name




