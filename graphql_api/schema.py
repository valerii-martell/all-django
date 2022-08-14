import graphene
from django.contrib.auth import get_user_model
from graphene_django.filter import DjangoFilterConnectionField

from .types import CarType, MakeType, ModelType  # , UserType
from .models import Car, Make, Model


class Query(graphene.ObjectType):
    make = graphene.relay.Node.Field(MakeType)
    makes = DjangoFilterConnectionField(MakeType)

    # make = graphene.Field(MakeType, id=graphene.Int())
    # makes = graphene.List(MakeType)

    # api_client = graphene.Field(UserType)
    # api_clients = graphene.List(UserType)

    model = graphene.Field(ModelType, id=graphene.Int())
    models = graphene.List(ModelType)
    car = graphene.Field(CarType, id=graphene.Int())
    cars = graphene.List(CarType, make=graphene.String())  # required=True)

    def __init__(self):
        dodge, _ = Make.objects.get_or_create(name="Dodge")
        chevrolet, _ = Make.objects.get_or_create(name="Chevrolet")
        ford, _ = Make.objects.get_or_create(name="Ford")

        charger, _ = Model.objects.get_or_create(name="Charger")
        chevelle, _ = Model.objects.get_or_create(name="Chevelle")
        mustang, _ = Model.objects.get_or_create(name="Mustang")

        Car.objects.get_or_create(license_plate="AA0000AA", notes="dodge notes", make=dodge, model=charger)
        Car.objects.get_or_create(license_plate="BB1110AA", notes="chevrolet notes", make=chevrolet, model=chevelle)
        Car.objects.get_or_create(license_plate="CC2210AA", notes="ford notes", make=ford, model=mustang)

        super().__init__()

    def resolve_model(self, info, **kwargs):
        id = kwargs.get('id', None)

        try:
            return Model.objects.get(id=id)
        except Model.DoesNotExist:
            return None

    def resolve_make(self, info, **kwargs):
        id = kwargs.get('id', None)

        try:
            return Make.objects.get(id=id)
        except Make.DoesNotExist:
            return None

    def resolve_car(self, info, **kwargs):
        id = kwargs.get('id', None)

        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            return None

    def resolve_makes(self, info, **kwargs):
        return Make.objects.all()

    def resolve_models(self, info, **kwargs):
        return Model.objects.all()

    def resolve_cars(self, info, make=None, **kwargs):
        if make:
            return Car.objects.filter(make__name=make)
        else:
            return Car.objects.all()

    def resolve_api_client(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        return user

    def resolve_api_clients(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        if not user.is_staff:
            raise Exception('Authentication Failure: Must be Manager')
        return get_user_model().objects.all()
