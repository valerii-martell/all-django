from graphql_api.models import Model, Make, Car
from orm.models import GamerLibraryModel, GamerModel, GameModel
from rest_framework import serializers
from django.contrib.auth.models import User


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'


class GamerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamerModel
        fields = ['nickname', 'email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'


class CarSerializer(serializers.HyperlinkedModelSerializer):
    make = serializers.PrimaryKeyRelatedField(
        queryset=Make.objects.all(),
    )

    model = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(),
    )

    class Meta:
        model = Car
        fields = ['license_plate', 'notes', 'make', 'model']
