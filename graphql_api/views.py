from django.shortcuts import render
from django.views import generic

from .models import Car, Make, Model


class Index(generic.TemplateView):
    template_name = 'graphql_index.html'

    # def get(self, request):
    #     return render(request, template_name=self.template_name, context={})
