from django.shortcuts import render
from django.views import generic

from .models import Car, Make, Model


class Index(generic.TemplateView):
    template_name = 'graphql_index.html'

    def __init__(self):
        dodge, _ = Make.objects.get_or_create(name="Dodge")
        chevrolet, _ = Make.objects.get_or_create(name="Chevrolet")
        ford, _ = Make.objects.get_or_create(name="Ford")

        charger, _ = Model.objects.get_or_create(name="Charger")
        chevelle, _ = Model.objects.get_or_create(name="Chevelle")
        mustang, _ = Model.objects.get_or_create(name="Mustang")

        Car.objects.get_or_create(license_plate="AA0000AA", notes="dodge notes", make=dodge, model=charger)
        Car.objects.get_or_create(license_plate="BB1110AA", notes="chevrolet notes", make=chevrolet, model=chevelle)
        Car.objects.get_or_create(license_plate="CC2210AA", notes="ford notes", make=ford, model=mustang)

        super().__init__()

    # def get(self, request):
    #     return render(request, template_name=self.template_name, context={})
