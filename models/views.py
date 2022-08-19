from django.shortcuts import render
import datetime, math
from django.http import HttpResponse
from django.template import loader

from .models import Flower, Bouquet, Client
from uuid import uuid4
from decimal import Decimal

from django.contrib.auth.models import User

from django.core.files import File


def models_index(request):
    _html = """
    <html>
        <head>
            <title>
                Django models
            </title>
        </head>
        <body>
            <h1>Models index:</h1>
            <p><a href="/">001. Back to main index</a></p>
            <p><a href="/admin/">002. Admin panel</a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)


def create_flower(request):
    rose = Flower()
    rose.description = (
        "Роза является представителем семейства Разноцветных,"
        " рода Шиповник. Растение в большинстве случаев "
        "представляет собой разветвленный кустарник, стебли"
        " которого покрыты шипами, роза имеет зеленые листья"
        " и большие ароматные цветы самого разного окраса"
    )
    rose.wiki_page = "ссылка на википедию"
    rose.name = "Роза красная"
    rose.save()
    return HttpResponse("Created!")


def create_client(request):
    # with open('requirements.txt', 'r') as _file:
    #     tmp_file = _file.read()

    client = Client.objects.create(
        **{
            "user": User.objects.get(pk=1),
            "second_email": "admin@admin1.com",
            "name": "MyName",
            # 'invoice': tmp_file,
            "invoice": File(open("requirements.txt")),
            "user_uuid": uuid4(),
            "discount_size": Decimal("0.00052"),
            "client_ip": "192.0.2.1.",
        }
    )
    return HttpResponse(client)


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)
