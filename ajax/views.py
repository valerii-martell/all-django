from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from .forms import UserCreateForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from orm.models import Human
from .forms import HumanForm
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


class MainView(TemplateView):
    template_name = "ajax.html"
    human_form = HumanForm

    def get(self, request):
        ctx = {}
        # ctx['script'] = 'alert(5555555);'
        if request.user.is_authenticated:
            all_humans = Human.objects.all()
            ctx["humans"] = all_humans
            ctx["human_form"] = self.human_form
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, ctx)


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/ajax/login"
    template_name = "register_ajax.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login_ajax.html"

    # В случае успеха перенаправим на главную.
    success_url = "/ajax/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_valid(form)


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/ajax/")


def validate_email(request):
    if request.GET:
        email = request.GET.get("email")
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            data = {
                "is_taken": "На этот почтовый ящик уже зарегистрирован пользователь!"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"ok": "На этот почтовый адрес не было регистраций"})


def show_three(request):
    first_three = Human.objects.all()[:3].values()
    context = {"elements": list(first_three)}
    return JsonResponse(context)


def show_four(request):
    last_four = Human.objects.all()[:4].values()

    context = {"elements": list(last_four)}
    return JsonResponse(context)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


@csrf_exempt
def add_human(request):
    if request.POST:
        if is_ajax(request):
            name = request.POST["name"]
            surname = request.POST["surname"]
            birth = request.POST["birth"]
            company = request.POST["company"]
            position = request.POST["position"]
            language = request.POST["language"]
            salary = request.POST["salary"]
            human = Human.objects.create(
                name=name,
                surname=surname,
                birth=birth,
                company=company,
                position=position,
                language=language,
                salary=salary,
            )
            return JsonResponse(human.dict())
