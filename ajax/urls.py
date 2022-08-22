from django.urls import path
from . import views


urlpatterns = [
    path("", views.MainView.as_view()),
    path("register/", views.RegisterFormView.as_view()),
    path("login/", views.LoginFormView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("validate-email/", views.validate_email),
    path("show-three/", views.show_three),
    path("show-four/", views.show_four),
    path("add-human/", views.add_human),
]
#
# urlpatterns = [
#
#     url(r'^$' , views.MainView.as_view()),
#     url(r'^register$' , views.RegisterFormView.as_view()),
#     url(r'^login$' , views.LoginFormView.as_view()),
#     url(r'^logout' , views.LogoutView.as_view()),
#     url(r'^validate-email' , views.validate_email),
#     url(r'^show-three' , views.show_three),
#     url(r'^show-four' , views.show_four),
#     url(r'^add-human/' , views.add_human),
#     ]
