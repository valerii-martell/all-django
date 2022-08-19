from django.contrib import admin
from django.urls import path
from frontend.views import (
    Index,
    Report,
    LoginExample,
    ListExample,
    DetailViewExample,
    DateDetailViewExample,
    WeekArchiveViewExample,
    DeleteExample,
    CreateViewExample,
    UpdateExample,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("report/", Report.as_view(), name="report"),
    path("login/", LoginExample.as_view(), name="login"),
    path("accounts/profile/", ListExample.as_view(), name="all_user"),
    path("detail/<pk>/", DetailViewExample.as_view(), name="detail"),
    path(
        "detail-date/<year>/<month>/<day>/<pk>",
        DateDetailViewExample.as_view(),
        name="detail_date",
    ),
    path("week-archive/<week>/", WeekArchiveViewExample.as_view(), name="week_archive"),
    path("create/", CreateViewExample.as_view(), name="create"),
    path("delete/<pk>/", DeleteExample.as_view(), name="delete"),
    path("update/<pk>/", UpdateExample.as_view(), name="update"),
]
