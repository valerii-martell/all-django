import csv
import datetime

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
# from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from .models import Human, GamerModel, GameModel, GamerLibraryModel


# Create your views here.


def index(request):
    _html = """
    <html>
        <head>
            <title>
                All Django - ORM
            </title>
        </head>
        <body>
            <h1>ORM index:</h1>
            <p><a href="/">001. Back to main index</a></p>
            <p><a href="/orm/list">002. List</a></p>
            <hr/>
            <p>Example 2:</p>
            <hr/>
            <p><a href="/orm/upload">003. Upload data</a></p>
            <p><a href="/orm/filter">004. Multiple filters</a></p>
            <p><a href="/orm/relation-filter">005. Relation filter (contains)</a></p>
            <p><a href="/orm/exclude">006. Exclude</a></p>
            <p><a href="/orm/orderby">007. Order by</a></p>
            <p><a href="/orm/all">008. All</a></p>
            <p><a href="/orm/union">009. Union</a></p>
            <p><a href="/orm/none">010. None</a></p>
            <p><a href="/orm/values">011. Values</a></p>
            <p><a href="/orm/dates">012. Dates</a></p>
            <p><a href="/orm/get">013. Get</a></p>
            <p><a href="/orm/create">014. Create</a></p>
        </body>
    </html>
    """
    return HttpResponse(_html)


class List(TemplateView):
    template_name = 'human_list.html'

    def get(self, request):

        # Human.objects.get(id=9).delete()
        all_humans = Human.objects.all()  # Все сотрудники
        the_first_two = Human.objects.all()[:2]
        workers_google = Human.objects.filter(company='google')
        filtered = Human.objects.filter(birth__year=1976)  # сотрудники 1976 года рождения
        one_worker = Human.objects.all()[0]
        ordered = Human.objects.all().order_by('-birth')
        sorted = Human.objects.filter(birth__year__lte=1980).order_by('birth')
        sorted_salary = Human.objects.filter(salary__gte=100, salary__lte=1000).delete()
        name_vasya = Human.objects.all().filter(name__contains='В')
        ctx = {
            'all_humans': all_humans,
            'workers_google': workers_google,
            'one_worker': one_worker,
            'filtered': filtered,
            'first_two': the_first_two,
            'ordered': ordered,
            'sorted': sorted,
            'sorted_salary': sorted_salary,
            'name_vasya': name_vasya

        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        query = request.POST['search']
        result_list = Human.objects.filter(company=query)
        if result_list.count() != 0:
            context = {
                'result_list': result_list,
                'query': query,
            }
        else:
            context = {
                'empty': "Ничего не найдено :(",
                'query': query,
            }
        return render(request, 'result.html', context)


def upload_data(request):
    # if not GameModel.objects.all():
    #     return HttpResponse(f"DB is already populated.")
    # else:
        GameModel.objects.all().delete()
        with open('orm/vgsales.csv') as f:
            reader = csv.reader(f)
            count = 0
            # TODO: bulk_create(list)
            to_create = []
            for row in reader:
                # print(row)
                try:
                    to_create.append(GameModel(
                        name=row[1],
                        platform=row[2],
                        year=datetime.date(int(row[3]), 1, 1),
                        genre=row[4],
                        publisher=row[5],
                        na_sales=row[6],
                        eu_sales=row[7],
                        jp_sales=row[8],
                        other_sales=row[9],
                        global_sales=row[10],
                    ))
                    # _, created = GameModel.objects.get_or_create(
                    #     name=row[1],
                    #     platform=row[2],
                    #     year=datetime.date(int(row[3]), 1, 1),
                    #     genre=row[4],
                    #     publisher=row[5],
                    #     na_sales=row[6],
                    #     eu_sales=row[7],
                    #     jp_sales=row[8],
                    #     other_sales=row[9],
                    #     global_sales=row[10],
                    # )
                    count += 1
                except Exception as error:
                    # print(error)
                    pass
            GameModel.objects.bulk_create(to_create)
        return HttpResponse(f"Done! Added {count} rows.")


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="A") & Q(name__endswith="a") & Q(
    #         name__contains="ma"))

    # queryset = GameModel.objects.filter(Q(name__endswith="a"),
    #                                     name__startswith="A")

    # queryset = GameModel.objects.filter(
    #     Q(name__startswith="Ab") | Q(name__startswith="Ad") | Q(
    #         name__startswith="Mat"))

    queryset = GameModel.objects.filter(
        ~Q(name__startswith="Ab") | ~Q(name__startswith="Ad") | ~Q(
            name__startswith="Mat"))


def relation_filter_view(request):
    data = GamerLibraryModel.objects.filter(gamer__email__contains="a")
    print(data[0].gamer.email)
    # return HttpResponse(data)
    return HttpResponse(data.order_by())


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains="Hitman")


class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # TODO add reverse
    queryset = GameModel.objects.exclude(name__contains="Hitman").order_by(
        'year')


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name="Hitman (2016)").union(
        GameModel.objects.filter(name="Tetris"))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'

    queryset = GameModel.objects.filter(name="Hitman (2016)").values("name",
                                                                     "platform",
                                                                     "year")

    def get(self, request, *args, **kwargs):
        print(GameModel.objects.filter(name="Hitman (2016)").values("name",
                                                                    "platform",
                                                                    "year"))
        print(list(
            GameModel.objects.all().values_list("name", 'year')))
        return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='year')
    print(data)
    return HttpResponse(data)


def get_view(request):
    # TODO try error
    data = GameModel.objects.get(id=27)
    print(data)
    return HttpResponse(data)


def create_view(request):
    # myself = GamerModel()
    # myself.email = "admin@admin.com"
    # myself.nickname = "SomeRandomNicknameSave"
    # myself.save()

    # myself = GamerModel(email="admin@admin.com",
    #                     nickname="SomeRandomNicknameSave")
    # myself.save()
    #
    # myself = GamerModel(**{"email": "admin@admin.com",
    #                        "nickname": "SomeRandomNicknameSave"})
    # myself.save()

    # myself = GamerModel.objects.create(**{"email": "admin@admin.com",
    #                                       "nickname": "SomeRandomNicknameCreate"})

    # myself = GamerModel.objects.create(email="admin@admin.com",
    #                                    nickname="SomeRandomNicknameCreate")
    # myself = GamerModel.objects.bulk_create([
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate1"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate2"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate3"),
    #     GamerModel(
    #         email="admin@admin.com", nickname="SomeRandomNicknameBulkCreate4")
    # ])

    # my_library = GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                                size=10)
    # my_library.save()
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.create(
    #     gamer=GamerModel.objects.get(pk=10),
    #     size=10)
    # my_library.game.set([GameModel.objects.get(pk=1),
    #                      GameModel.objects.get(pk=2)])

    # my_library = GamerLibraryModel.objects.bulk_create(
    #     [GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10),
    #      GamerLibraryModel(gamer=GamerModel.objects.get(pk=10),
    #                        size=10)
    #      ])
    my_friend = GamerModel.objects.get(pk=10)
    my_friend.update(nickname="MySecondNickname")
    return HttpResponse(my_friend)
