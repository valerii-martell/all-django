from django.http import (
    HttpResponse,
    FileResponse,
    HttpResponseRedirect,
    HttpResponseNotAllowed,
    JsonResponse,
)
from django.shortcuts import render
from django.templatetags.static import static
from django.views import View
from django.template import loader


def routing_index(request):
    return render(request, "routing_index.html", {})


def http_redirect(request):
    # return redirect("/")
    return HttpResponseRedirect("http://www.google.com")


def file_response(request):
    # with open() as file:
    #     work with file
    # print(static('images/001.jpg')[1:])
    return FileResponse(open(static("images/001.jpg")[1:], "rb+"))


def function(request, year=1111, month=11, day=1):
    return HttpResponse(
        "Parameters {year}/{month}/{day}".format(year=year, month=month, day=day)
    )


def render_html(request):
    _html = """
    <html>
        <head>
            <title>
                Django routing
            </title>
        </head>
        <body>
            <h1>Rendered HTML</h1>
        </body>
    </html>
    """

    return HttpResponse(_html)


def render_template(request):
    return render(request, "routing/main.html", {})


def request_properties(request):
    _html = """
    <html>
        <head>
            <title>
                Request parameters
            </title>
        </head>
        <body>
            <h1>Request parameters</h1>
            <p>Path: {0}</p>,
            <p>Full path: {1}</p>,
            <p>Host: {2}</p>,
            <p>Is secure (hhtps): {3}</p>,
        </body>
    </html>
    """.format(
        request.path, request.get_full_path(), request.get_host(), request.is_secure()
    )

    return HttpResponse(_html)


def render_to_string(request):
    test_template = loader.render_to_string("routing/main.html")
    return HttpResponse(test_template)


def text(request):
    return HttpResponse("This is text from backend to user interface")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)


def api(request):
    return JsonResponse({"subdomain": "api"}, safe=False)


def beta(request):
    return HttpResponse("Beta subdomain")
