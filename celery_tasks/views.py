from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView, ListView

from all_django.settings import SESSION_COOKIE_AGE
from celery_tasks.forms import TotalForm
from .models import Bot
from .tasks import create_bot


class Index(TemplateView):
    template_name = "celery_index.html"


class GenerateBotView(FormView):
    template_name = "farm/bots_form.html"
    form_class = TotalForm

    def form_valid(self, form):
        total_by_user = self.request.session.get("total_by_user", 0)
        self.request.session["total_by_user"] = total_by_user + form.cleaned_data.get(
            "total"
        )
        create_bot.delay(form.cleaned_data.get("total"))
        messages.success(
            self.request,
            f"Generating your random bots. "
            f"Please, wait a moment and refresh this page. "
            f"During the session ({SESSION_COOKIE_AGE} sec) you have requested totally "
            f'{self.request.session.get("total_by_user")} bots.',
        )
        return redirect("bots_list")


class BotsListView(ListView):
    template_name = "farm/bots_list.html"
    model = Bot
