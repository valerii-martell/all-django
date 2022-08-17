"""all_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from all_django import settings

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('', include("index.urls")),
    path('smoke/', include("smoke.urls")),
    path('routing/', include("routing.urls")),
    path('views/', include("views.urls")),
    path('templates/', include("templates.urls")),
    path('models/', include("models.urls")),
    path('forms/', include("forms.urls")),
    path('orm/', include("orm.urls")),
    path('authentication/', include("authentication.urls")),
    path('ajax/', include("ajax.urls")),
    path('api/', include("api.urls")),
    path('security/', include("security.urls")),
    path('custom-user/', include("custom_user.urls")),
    path('custom-admin/', include("custom_admin.urls")),
    path('frontend/', include("frontend.urls")),
    path('emails/', include("emails.urls")),
    path('graphql/', include("graphql_api.urls")),
    path('celery/', include("celery_tasks.urls")),
    path('channels/', include("channels_app.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
