from django.shortcuts import render, redirect
from django.http import HttpResponse


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
            <p><a href="/routing/file-response">003. File Response TODO</a></p>
            <p><a href="/routing/function/1996/08/30">004. Function with parameters /year/month/day or / - default values </a></p>
            <p><a href="/routing/render-html">005. Render HTML string </a></p>
            <p><a href="/routing/render-template">006. Render HTML template </a></p>
            <p><a href="/routing/request-properties">007. Request additional properties </a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)


def http_redirect(request):
    return redirect("/")


def file_response(request):
    return redirect("/")
    pass


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
    return render(request, 'routing.html', {})


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
