from django.urls import path
from . import views
from authentication.views import RegisterFormView, LogoutView, LoginFormView

urlpatterns = [
    path('', views.channels_index, name='channels_index'),
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('register/', RegisterFormView.as_view()),
    path('login/', LoginFormView.as_view()),
    path('logout/', LogoutView.as_view()),
]