from django.db import models
from django.utils.html import format_html


class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Promo(models.Model):
    promo_type = models.CharField(max_length=128)
    description = models.TextField()
    end_time = models.DateField(null=True)
    start_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.promo_type


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):
    description = models.TextField()
    model = models.CharField(max_length=128)
    price = models.FloatField()
    color = models.CharField(max_length=30)
    warranty = models.IntegerField()
    count = models.IntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    promo = models.ManyToManyField(Promo)

    def __str__(self):
        return f'{self.brand_name} {self.model}'


class Notebook(Item):
    display = models.DecimalField(max_digits=5, decimal_places=4)
    memory = models.IntegerField()
    video_memory = models.IntegerField()
    cpu = models.CharField(max_length=128)


class Dishwasher(Item):
    energy_saving_class = models.CharField(max_length=2, default='A+')
    power = models.IntegerField(default=0)
    width = models.FloatField()
    height = models.FloatField()

    def colored_name(self):
        return format_html(
            '<span style="color: #ff0FFF;">{} {}</span>',
            self.model,
            self.brand_name,
        )


class VacuumCleaner(Item):
    noise_level = models.FloatField()
    power = models.IntegerField()
    width = models.FloatField()
    height = models.FloatField()
    eco_engine = models.BooleanField(default=False)


class TV(Item):
    display = models.DecimalField(max_digits=5, decimal_places=4)
    memory = models.IntegerField()
    display_type = models.CharField(max_length=8)
    smart_tv = models.BooleanField(False)