from django.db import models


class PersonManager(models.Manager):

    def get_staff_users(self):
        return super(PersonManager, self).get_queryset().filter(is_staff=False)
