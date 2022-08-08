from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'game', views.GameViewSet)
router.register(r'gamer', views.GamerViewSet)


urlpatterns = [
    path('', views.api_index),
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/',
#          include('rest_framework.urls', namespace='rest_framework'))
# ]