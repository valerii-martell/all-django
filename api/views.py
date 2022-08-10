from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from orm.models import GameModel, GamerModel
from .serializers import GameModelSerializer, GamerModelSerializer, UserSerializer


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
            <p><a href="/api/function">002. Function-based API view</a></p>
            <p><a href="/api/class">003. CLass-based API view</a></p>
            <p><a href="/api/game">004. API ViewSet - games (default)</a></p>
            <p><a href="/api/gamer">005. API ViewSet - gamers (default)</a></p>
            <p><a href="/api/view-set">006. API ViewSet - list, retrieve all or by id</a></p>
            <p><a href="/api/create">007. Generic API view - create</a></p>
            <p><a href="/api/retrieve/1">008. Generic API view - retrieve by id</a></p>
            <p><a href="/api/retrieve-update/1">009. Generic API view - retrieve and update by id</a></p>
            <p><a href="/api/register">010. API new user register - function-based view + token</a></p>
            <p><a href="/api/login">011. API user login - generic API view</a></p>
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


class ViewSetAPIView(viewsets.ViewSet):
    queryset = GameModel.objects.filter(id__lte=10)

    def list(self, request):
        serializer = GameModelSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = GameModelSerializer(user)
        return Response(serializer.data)


class MyCreateAPIView(CreateAPIView):
    serializer_class = GamerModelSerializer


class MyRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer


class MyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = GamerModel.objects.all()
    serializer_class = GamerModelSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Both username and password are required'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid data'})

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


class CreateUser(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
