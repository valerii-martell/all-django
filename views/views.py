from django.http import HttpResponse, FileResponse, HttpResponseRedirect, \
    HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static

from django.views import View

from django.template import loader


def views_index(request):
    _html = """
        <html>
            <head>
                <title>
                    Django routing
                </title>
            </head>
            <body>
                <h1>Views index:</h1>
                <p><a href="/">001. Back to main index</a></p>
                <p><a href="/views/function-view">002. Function-based view</a></p>
                <p><a href="/views/class-view">003. Class-based view</a></p>
            </body>
        </html>
        """
    return HttpResponse(_html)


class MyView(View):

    def get(self, request):
        if request.GET.get('type') == "file":
            return FileResponse(open(static('images/user.png')[1:], "rb+"), )
        elif request.GET.get('type') == "json":
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == "redirect":
            return HttpResponseRedirect("https://www.google.com")
        else:
            _html = """
                    <html>
                        <head>
                            <title>
                                Class-based view index
                            </title>
                        </head>
                        <body>
                            <h1>Class-based view index:</h1>
                            <p><a href="/views">001. Back to main views index</a></p>
                            <p><a href="/views/class-view?type=file">002. File</a></p>
                            <p><a href="/views/class-view?type=json">003. JSON</a></p>
                            <p><a href="/views/class-view?type=redirect">004. Redirect</a></p>
                        </body>
                    </html>
                    """
            return HttpResponse(_html)

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")


def function_view(request):
    test_template = loader.render_to_string("main.html")
    return HttpResponse(test_template)


def text(request):
    return HttpResponse("This is text from backend to user interface")


def file(request):
    # with open() as file:
    #     work with file
    print(static('img/001.jpg'))
    return FileResponse(open(static('images/001.jpg'), "rb+"))


def redirect(request):
    return HttpResponseRedirect("https://www.google.com")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)