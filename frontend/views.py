import json
import random
import urllib.request

from django.views.generic import (TemplateView, ListView, DetailView, DateDetailView,
                                  WeekArchiveView, DeleteView, CreateView, UpdateView, FormView)
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm

url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        return {'some_data': [random.choice(words)
                              for i in range(10)]}


class Report(TemplateView):
    template_name = 'main/report.html'


class LoginExample(LoginView):
    pass


class ListExample(ListView):
    template_name = 'accounts/profile.html'
    queryset = User.objects.all()
    context_object_name = "users"


class DetailViewExample(DetailView):
    template_name = 'detail.html'
    model = User


class DateDetailViewExample(DateDetailView):
    template_name = 'date_detail.html'
    model = User
    date_field = "date_joined"


# Example http://127.0.0.1:8000/detail-date/2020/feb/24/2


class WeekArchiveViewExample(WeekArchiveView):
    template_name = 'week_archive.html'
    year = 2022
    model = User
    date_field = "date_joined"
    context_object_name = "week_users_archive"
#     http://127.0.0.1:8000/detail-date/2020/feb/24/2


class CreateViewExample(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


class UpdateExample(UpdateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


class DeleteExample(DeleteView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'
