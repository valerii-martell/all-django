from django.contrib.auth.models import User
from .managers import PersonManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


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


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email'), unique=True)
#     first_name = models.CharField(_('name'), max_length=30, blank=True)
#     last_name = models.CharField(_('surname'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
#     is_active = models.BooleanField(_('is_active'), default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#
#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         return self.first_name
#
#     def email_user(self, subject, message, from_email=None, **kwargs):
#         send_mail(subject, message, from_email, [self.email], **kwargs)