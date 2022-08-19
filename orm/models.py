from django.db import models

# Create your models here.


class Human(models.Model):

    CHOICE_COMPANY = (
        ("google", "Google"),
        ("yandex", "Yandex"),
        ("itvdn", "Itvdn"),
        ("epam", "Epam"),
    )
    POSITION_CHOICES = (
        ("senior", "Senior"),
        ("middle", "Middle"),
        ("junior", "Junior"),
    )

    PYTHON = "python"
    JAVASCRIPT = "javascript"
    CS = "c#"
    CPP = "cpp"

    LANGUAGE_CHOICES = (
        (PYTHON, "Python"),
        (JAVASCRIPT, "Javascript"),
        (CS, "C#"),
        (CPP, "C++"),
    )
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    birth = models.DateField(auto_now_add=False, auto_now=False)
    company = models.CharField(max_length=150, choices=CHOICE_COMPANY)
    position = models.CharField(max_length=15, choices=POSITION_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default=PYTHON)
    salary = models.IntegerField()

    def __str__(self):
        return "Имя  - {0} , Фамилия -  {1} , Компания - {2}".format(
            self.name, self.surname, self.company
        )

    def dict(self):
        obj = {
            "name": self.name,
            "surname": self.surname,
            "birth": self.birth,
            "company": self.company,
            "position": self.position,
            "language": self.language,
            "salary": self.salary,
        }
        return obj


class GameModel(models.Model):
    name = models.CharField(max_length=64)
    platform = models.CharField(max_length=64)
    year = models.DateField()
    genre = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()

    def __str__(self):
        return f"{self.id}_{self.name}"


class GamerLibraryModel(models.Model):
    game = models.ManyToManyField("GameModel")
    gamer = models.ForeignKey("GamerModel", on_delete=models.DO_NOTHING)
    size = models.IntegerField()

    def __str__(self):
        return f"{self.id}_{self.gamer.nickname}"


class GamerModel(models.Model):
    nickname = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id}_{self.nickname}"


# GamerModel.objects = GamerModel.objects.using('postgresql')
# GamerLibraryModel.objects = GamerLibraryModel.objects.using('postgresql')
# GameModel.objects = GameModel.objects.using('postgresql')
