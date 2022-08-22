from django.urls import path
from . import views
from all_django.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Index.as_view()),
    path("signup-proxy/", views.CreatUserProxy.as_view()),
    path("all-staff-users/", views.AllStaffUsers.as_view()),
    path("signup/", views.CreatUser.as_view()),
    path("all-users/", views.AllUsers.as_view()),
    path("profile/<pk>", views.UpdateProfile.as_view()),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
