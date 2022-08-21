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

from orm.models import GamerModel, GameModel


def security_test(request):
    # print(request.POST.get('user_input_js'))
    # print(request.POST.get('user_input_sql'))

    my_variable_js = (
        request.POST.get("user_input_js")
        if request.POST.get("user_input_js") == 'alert("hacked");'
        else 'alert("secured");'
    )
    my_variable_sql = (
        request.POST.get("user_input_sql")
        if request.POST.get("user_input_sql")
        == "SELECT * FROM public.orm_gamemodel LIMIT 1;"
        else None
    )
    # TODO: public for postgresql, main for sqllite

    try:
        result_sql = GameModel.objects.raw(my_variable_sql)
        result = [result for result in result_sql]
    except:
        result = []

    return render(
        request,
        "security_test.html",
        context={"my_variable_js": my_variable_js, "my_variable_sql": result},
    )


def ajax_check(request):
    return JsonResponse({"result": "success"}, safe=False)
