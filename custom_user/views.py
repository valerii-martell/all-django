from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import FormView
from .models import Person


class Index(TemplateView):
    template_name = 'custom_user_index.html'


class CreatUser(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(CreatUser, self).form_valid(form)


class AllUsers(TemplateView):
    template_name = "all_users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['users'] = Person.people.get_staff_users()
        return context
