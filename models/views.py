from django.shortcuts import render
import datetime , math
from django.http import HttpResponse
from django.template import loader


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

