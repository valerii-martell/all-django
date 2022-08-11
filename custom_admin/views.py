from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from django.views.generic import FormView


class Index(TemplateView):
    template_name = 'custom_admin_index.html'
