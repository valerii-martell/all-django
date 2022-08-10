from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'game', views.GameViewSet)
router.register(r'gamer', views.GamerViewSet)
router.register(r'view-set', views.ViewSetAPIView)

urlpatterns = [
    path('', views.api_index),
    path('', include(router.urls)),
    path('function/', views.view_function, name='function_view'),
    path('class/', views.ClassAPIView.as_view(), name='class_view'),
    path('create/', views.MyCreateAPIView.as_view(), name='create'),
    path('retrieve/<int:pk>', views.MyRetrieveAPIView.as_view(), name='retrieve'),
    path('retrieve-update/<int:pk>', views.MyRetrieveUpdateAPIView.as_view(),
         name='retrieve_update'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', views.user_login),
    path('register', views.CreateUser.as_view())
]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/',
#          include('rest_framework.urls', namespace='rest_framework'))
# ]
