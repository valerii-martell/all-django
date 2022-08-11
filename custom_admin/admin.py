from django.contrib import admin
from .models import TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Item, Promo


# for model in [TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Promo]:
#     admin.site.register(model)
class DishwasherInstanceInline(admin.TabularInline):
    model = Dishwasher


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [DishwasherInstanceInline]


@admin.register(Dishwasher)
class DishwasherAdmin(admin.ModelAdmin):
    class Media:
        css = {}

    list_display = ('model', 'brand_name', 'price',
                    'color', 'test_show_promo', 'colored_name')
    list_filter = ('price', 'brand_name', 'color',)
    fieldsets = (
        ('General info', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'model'),
        }),
        ('Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color'),
        }),)
    sortable_by = 'price'
    search_fields = ['brand_name__pk']
    # exclude = ('price',)
    empty_value_display = '-Без бренда-'
    readonly_fields = ['price']

    def test_show_promo(self, obj):
        return obj.promo

    def delete_model(self, request, obj):
        pass
