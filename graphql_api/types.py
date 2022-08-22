import graphene
from django.contrib.auth import get_user_model

from graphene_django import DjangoObjectType
from .models import Car, Make, Model


class MakeType(DjangoObjectType):
    class Meta:
        model = Make
        fields = ("id", "name")
        # filter_fields = ("name", "id")
        filter_fields = {"name": ["exact", "icontains", "istartswith"]}
        interfaces = (graphene.relay.Node,)


class ModelType(DjangoObjectType):
    class Meta:
        model = Model
        fields = ("id", "name")


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "license_plate", "make", "model")


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
