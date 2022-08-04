from django.http import HttpResponse, FileResponse, HttpResponseRedirect, \
    HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views import View
from django.template import loader


def routing_index(request):
    _html = """
    <html>
        <head>
            <title>
                Django routing
            </title>
        </head>
        <body>
            <h1>Routing index:</h1>
            <p><a href="/">001. Back to main index</a></p>
            <p><a href="/routing/redirect">002. Redirect</a></p>
            <p><a href="/routing/text">003. Text Response</a></p>
            <p><a href="/routing/file-response">004. File Response</a></p>
            <p><a href="/routing/json">005. JSON Response</a></p>
            <p><a href="/routing/not-allowed">006. Not allowed</a></p>
            <p><a href="/routing/function/1996/08/30">007. Function with parameters /year/month/day or / - default values </a></p>
            <p><a href="/routing/render-html">008. Render HTML string </a></p>
            <p><a href="/routing/render-template">009. Render HTML template </a></p>
            <p><a href="/routing/render-to-string">010. Render to string </a></p>
            <p><a href="/routing/request-properties">011. Request additional properties </a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)


def http_redirect(request):
    # return redirect("/")
    return HttpResponseRedirect("http://www.google.com")


def file_response(request):
    # with open() as file:
    #     work with file
    # print(static('images/001.jpg')[1:])
    return FileResponse(open(static('images/001.jpg')[1:], "rb+"))


def function(request, year=1111, month=11, day=1):
    return HttpResponse("Parameters {year}/{month}/{day}".format(year=year, month=month, day=day))


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
    return render(request, 'main.html', {})


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
    """.format(request.path, request.get_full_path(), request.get_host(), request.is_secure())

    return HttpResponse(_html)


def render_to_string(request):
    test_template = loader.render_to_string("main.html")
    return HttpResponse(test_template)


def text(request):
    return HttpResponse("This is text from backend to user interface")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
