from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from all_django import settings
from .views import Index, SendMailView, ShowMailView, usersignup, activate_account, subscription
from django.contrib.auth import views as auth

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', Index.as_view()),
    path('show-mail/', ShowMailView.as_view()),
    path('send-mail/', SendMailView.as_view()),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path(r'signup/', usersignup, name='register_user'),
    path(r'activate/<uidb64>/<token>/', activate_account, name='activate'),
    path("subscription/", subscription, name="subscription"),
]
