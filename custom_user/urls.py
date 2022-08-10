from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('signup/', views.CreatUser.as_view(), name="signup"),
    path('all-users/', views.AllUsers.as_view(), name="all_users")
]