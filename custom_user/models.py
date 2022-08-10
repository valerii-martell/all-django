from django.contrib.auth.models import User
from .managers import PersonManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


class Person(User):
    people = PersonManager()

    class Meta:
        proxy = True
        ordering = ('first_name',)

    def do_something(self):
        print(self.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    birthday = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=150)
    photo = models.ImageField(upload_to='profile_pics')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()