from django.urls import path
from . import views
from .views import GenerateBotView, BotsListView


urlpatterns = [
    path("", views.Index.as_view()),
    path("generate/", GenerateBotView.as_view(), name="generate"),
    path("bots-list/", BotsListView.as_view(), name="bots_list"),
]
