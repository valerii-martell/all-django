from django.http import HttpResponse


def smoke(request):
    return HttpResponse("Smoke")
