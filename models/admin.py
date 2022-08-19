from django.contrib import admin
from . import models

admin.site.register(models.Example)

admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)
admin.site.register(models.Client)
admin.site.register(models.Flower)
admin.site.register(models.Bouquet)


#
class AuthorAdmin(admin.ModelAdmin):
    # list_display = ['name' , 'surname']
    list_display = [field.name for field in models.Author._meta.fields]
    # exclude = ["name"] # hide mentioned fields
    fields = ["name", "surname"]  # show mentioned fields
    list_filter = ["name"]
    # search_fields = ['name' , 'surname']
    search_fields = [field.name for field in models.Author._meta.fields]

    class Meta:
        model = models.Author


admin.site.register(models.Author, AuthorAdmin)
