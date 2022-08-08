import os

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from all_django import settings
from . import forms
from django.core.mail import send_mail
from . import models
from django.views import generic

# Create your views here.

from django.shortcuts import render

from .forms import MyForm, FormFromModel


def forms_index(request):
    return render(request, "index.html", {})


def search_form(request):
    if request.method == "GET":
        if len(request.GET) == 0:
            return render(request, 'search_form.html', {})
        elif 'query' in request.GET:
            return HttpResponse("You're trying to find: %s" % request.GET['query'])
        else:
            return HttpResponse("You've sent an empty form")


def file_input(request):
    if request.method == "GET":
        return render(request, 'file_form.html', {})
    else:
        name = request.POST['name']
        surname = request.POST['surname']
        birth = request.POST['birth']
        gender = request.POST['gender']
        # some_file = open("some.txt", "w")
        with open("some.txt", "w") as some_file:
            some_file.write("Name :" + name + "\n")
            some_file.write("Surname :" + surname + "\n")
            some_file.write("Date of birth :" + birth + "\n")
            some_file.write("Gender :" + gender + "\n")
        return HttpResponse("The data was recorded successfully!")


def model_input(request):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm
    context = {
        'form_for_author1': form_for_author1,
        'form_for_article': form_for_article,
        'form_contact': form_contact
    }
    return render(request, 'form.html', context)


def add_author(request):
    form = forms.AuthorOneForm(request.POST)
    result = "An author has been added successfully %s" % request.path
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse("Автор добавлен! %s" % request.path)


def add_article(request):
    form = forms.ArticleForm(request.POST)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        form = form.save()
        return HttpResponse("Статья добавлена!")


class ContactFormView(generic.TemplateView):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': form,

        }
        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request, 'form.html', context)

    def get(self, request):
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': self.form_contact
        }
        return render(request, 'form.html', context)


class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm

    def get(self, request):
        context = {
            'form_url': self.form_submit_url
        }
        return render(request, 'url_form.html', context)

    def post(self, request):
        form = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print('invalid')
            context = {
                'form_url': form
            }
            return render(request, 'url_form.html', context)
        return HttpResponse(form.cleaned_data.items())


def function_form(request):
    print(request.FILES)
    form = MyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        print(form.cleaned_data)
        file_path = os.path.join(settings.MEDIA_ROOT,
                                 form.cleaned_data['profile_picture'].name)
        with open(file_path, 'wb+') as local_file:
            for chunk in form.cleaned_data['profile_picture']:
                local_file.write(chunk)
    else:
        print(form.errors)

    return render(request, 'form_page.html', context={'form': form})


class ClassFormView(FormView):
    form_class = MyForm
    template_name = "form_page.html"

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return super().get(request, *args, **kwargs)


class ModelFormView(FormView):
    form_class = FormFromModel
    template_name = "model_from_page.html"
    success_url = reverse_lazy("model_form")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)