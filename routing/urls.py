from django.urls import path
from . import views

urlpatterns = [
    path("", views.routing_index, name="routing_index"),
    path("redirect/", views.http_redirect, name="redirect"),
    path("file-response/", views.file_response, name="file"),
    path("function/", views.function),
    path("function/<int:year>/<int:month>/<int:day>/", views.function),
    path("render-html/", views.render_html),
    path("render-template/", views.render_template, name="render_template"),
    path("request-properties/", views.request_properties),
    path("not-allowed/", views.not_allowed, name="not_allowed"),
    path("render-to-string/", views.render_to_string, name="render_to_string"),
    path("text/", views.text, name="text"),
    path("json/", views.json, name="json"),
]
