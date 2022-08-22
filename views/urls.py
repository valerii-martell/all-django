from django.urls import path
from . import views

urlpatterns = [
    path("", views.views_index),
    path("function-view/", views.function_view),
    path("function-view/text/", views.text, name="text"),
    path("function-view/file/", views.file, name="file"),
    path("function-view/redirect/", views.redirect, name="redirect"),
    path("function-view/not-allowed/", views.not_allowed, name="not_allowed"),
    path("function-view/json/", views.json, name="json"),
    path("class-view/", views.MyView.as_view(), name="class_view"),
]
