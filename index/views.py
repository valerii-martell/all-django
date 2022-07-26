from django.http import HttpResponse


def index(request):
    _html = """
    <html>
        <head>
            <title>
                All Django
            </title>
        </head>
        <body>
            <h1>Index:</h1>
            <p><a href="/smoke">001. Smoke</a></p>
            <p><a href="/routing">002. Routing</a></p>
            <p><a href="/templates">003. Templates</a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)
