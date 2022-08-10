from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]

#
# urlpatterns = [
#
#     url(r'^register/$', views.RegisterFormView.as_view()),
#     url(r'^login/$', views.LoginFormView.as_view()),
#     url(r'^logout/$', views.LogoutView.as_view()),
#     url(r'^$', views.MainView.as_view()),
#
# ]