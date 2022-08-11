from django.shortcuts import render
import datetime, math
from django.http import HttpResponse
from django.template import loader


def templates_index(request):
    _html = """
    <html>
        <head>
            <title>
                Django templates
            </title>
        </head>
        <body>
            <h1>Templates index:</h1>
            <p><a href="/">001. Back to main index</a></p>
            <p><a href="/templates/filters">002. Filters + custom filters</a></p>
            <p><a href="/templates/tags-if">003. Tags if </a></p>
            <p><a href="/templates/tags-for">004. Tags for + custom tags</a></p>
            <p><a href="/templates/regroup">005. Tags regroup </a></p>
            <p><a href="/templates/base">006. Tags include and extend </a></p>
            <p><a href="/templates/jinja2">007. Jinja2 </a></p>
        </body>
    </html>
    """

    return HttpResponse(_html)


# def view(request):
#     list  = [0,232,45,123,4,53423,54,23]
#     template  = loader.get_template('index.html')
#     context = {
#         "test": "TEXT!",
#         "list": list,
#         "name": "Valerii",
#         "surname": "Martell",
#         "coords": {
#             "x": "x coords",
#             "y": "y coords",
#         },
#         # 'list': [1,2,3,4]
#     }
#     return HttpResponse(template.render(context, request))


def context(request):
    list = [0, 232, 45, 123, 0, 4, 53423, 54, 23]
    context = {
        "test": "TEXT!",
        "list": list,
        "name": "Valerii",
        "surname": "Martell",
        "coords": {
            "x": "x coords",
            "y": "y coords",
        },
        # 'list': [1,2,3,4]
    }
    return render(request, "context.html", context)


def filter(request):
    array_for_sort = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    context = {
        "name_low": "LOWER",
        "value": 9,
        "first": [1, 2, 3, 4],
        "second": [5, 6, 7, 8],
        "str": "I'm using Django",
        "date": datetime.datetime.now(),
        "empty_one": "",
        "for_sort": array_for_sort,
        "float": 32.223,
        "number": 12345678,
        "boolean_var": None,
        'name': "alex"
    }
    return render(request, "filter.html", context)


def tags_if(request):
    list = [1, 2, 3, 4, 5, 6]
    var1 = "var1"
    var2 = "var2"
    var3 = "var3"
    obj = {
        'name': "Alex",
        'surname': "Parker"
    }
    context = {
        "x": "x value",
        'user': "Admin",
        'list': list,
        'value': 10,
        'obj': obj,
        # 'var' : "var1",
        "greetings": ["hello", "abc", "xsa"],
        "a": 100,
        "b": 10,
        "c": 1,
        # 'var' : "var2",
    }
    return render(request, 'tags_if.html', context)


def tags_for(request):
    list = [1, 2, 3, 4, 5, 6]
    empty = []
    context = {
        "list": list,
        'empty': empty,
    }
    return render(request, 'tags_for.html', context)


def tag_regroup(request):
    people = [
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
    ]
    people_for_test = [
        {'first_name': 'Bill', 'last_name': 'Clinton', 'gender': 'Male'},
        {'first_name': 'Pat', 'last_name': 'Smith', 'gender': 'Unknown'},
        {'first_name': 'Margaret', 'last_name': 'Thatcher', 'gender': 'Female'},
        {'first_name': 'George', 'last_name': 'Bush', 'gender': 'Male'},
        {'first_name': 'Condoleezza', 'last_name': 'Rice', 'gender': 'Female'},
    ]
    context = {
        "people": people,
        "people_for_test": people_for_test,
    }
    return render(request, 'regroup.html', context)


def base(request):
    context = {}
    return render(request, 'base.html', context)


def adrian(request):
    context = {
        'name': 'Адриан',
        'surname': 'Головатый',
    }
    return render(request, "adrian.html", context)


def realese(request):
    obj = (
        {"year": 2015, "version": "1.8"},
        {"year": 2016, "version": "1.9"},
        {"year": "2016-2017", "version": "1.10"},
        {"year": 2017, "version": "1.11"},
        {"year": 2018, "version": "2.0"},
    )

    context = {
        'obj': obj,
    }
    return render(request, "realese.html", context)


def jinja(request):
    context = {
        'my_string': "Wheeeee!",
        'my_list': [0,1,2,3,4,5],
        'data':
            {'key': 'Jinja2'}
    }
    return render(request, "jinja2/jinja2.html", context, using='jinja2')
