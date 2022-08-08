from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from orm.models import GameModel, GamerModel
from .serializers import GameModelSerializer, GamerModelSerializer


def api_index(request):
    _html = """
    <html>
        <head>
            <title>
                Django REST Framework
            </title>
        </head>
        <body>
            <h1>Django REST Framework index:</h1>
            <p><a href="/">001. Back to main index</a></p>
            <p><a href="/api/game">002. Games list</a></p>
            <p><a href="/api/gamer">003. Gamers list</a></p>
            <hr/>
            <p><a href="/api/function">004. Function-based API view</a></p>
            <p><a href="/api/class">005. CLass-based API view</a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all().order_by('-year')
    serializer_class = GameModelSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
# @api_view()
def view_function(request):
    # print(request.data)
    return Response({'test': 'some_function_data'})


class ClassAPIView(APIView):

    def get(self, request):
        return Response({'class': 'some_class_data'})

    def post(self, request):
        # print(request.data)
        return Response({'class': 'some_class_data'})
