import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token

from .types import MakeType, UserType
from .models import Make


class MakeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class CreateMake(graphene.Mutation):
    class Arguments:
        input = MakeInput(required=True)

    ok = graphene.Boolean()
    make = graphene.Field(MakeType)

    @classmethod
    def mutate(cls, root, info, input=None):
        ok = True
        make_instance = Make.objects.create(name=input.name)
        return cls(ok=ok, make=make_instance)


class UpdateMake(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MakeInput(required=True)

    ok = graphene.Boolean()
    make = graphene.Field(MakeType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        ok = False
        try:
            make_instance = Make.objects.get(pk=id)
        except Make.DoesNotExist:
            return cls(ok=ok, make=None)

        ok = True
        make_instance.name = input.name
        make_instance.save()
        return cls(ok=ok, make=make_instance)


class DeleteMake(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            make_instance = Make.objects.get(pk=id)
            make_instance.delete()
            return cls(ok=True)
        except Make.DoesNotExist:
            return cls(ok=False)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        username = graphene.String(required=True)

    def mutate(self, info, password, username, email):
        user = get_user_model()(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()

        token = get_token(user)
        refresh_token = create_refresh_token(user)

        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class Mutation(graphene.ObjectType):
    create_make = CreateMake.Field()
    update_make = UpdateMake.Field()
    delete_make = DeleteMake.Field()
    create_user = CreateUser.Field()
