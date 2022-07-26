from django.urls import path
from . import views

urlpatterns = [
    path('', views.routing_index),
    path('redirect/', views.http_redirect),
    path('file-response/', views.file_response),
    path('function/', views.function),
    path('function/<int:year>/<int:month>/<int:day>/', views.function),
    path('render-html/', views.render_html),
    path('render-template/', views.render_template),
]