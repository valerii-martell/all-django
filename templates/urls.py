from django.urls import path
from . import views

urlpatterns = [
    path('', views.templates_index),
    path('context/', views.context),
    path('filters/', views.filter),
    path('tags-if/', views.tags_if),
    path('tags-for/', views.tags_for),
    path('regroup/', views.tag_regroup),
    path('base/', views.base),
    path('adrian/', views.adrian),
    path('realese/', views.realese),
    path('jinja2/', views.jinja),
]
