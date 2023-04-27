from django.contrib import admin
from .models import Category, Product, Dopolnenie

class DopInLine(admin.TabularInline):
    model = Dopolnenie
    extra = 0

class DopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dopolnenie._meta.fields]
admin.site.register(Dopolnenie, DopAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug', 'price', 'stock', 'dop1', 'dop2','description', 'weight', 'available', 'created', 'updated']
    # list_display = ['name', 'slug','dop1', 'price', 'stock','description', 'weight', 'available', 'created', 'updated']
    list_display = ['name', 'slug','price_dop1', 'price', 'description', 'weight', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'description', 'weight']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DopInLine]

    def price_dop1(self, obj):
        if obj.dopolnenie:
           return obj.dopolnenie.price_dop1
        return None
    price_dop1.short_description = 'price_dop1'

    # def dop2(self, obj):
    #     return obj.dop.dop2
    # dop2.short_description = 'Dopol2'
  
    # def dop1(self, obj):
    #     if obj.dop:
    #         return obj.dop.dop1
    #     return None

    # def dop2(self, obj):
    #     if obj.dop:
    #         return obj.dop.dop2
    #     return None
    
    # dop1.short_description = 'Dop1'
    # dop2.short_description = 'Dop2'


admin.site.register(Product, ProductAdmin)

# https://pocoz.gitbooks.io/django-v-primerah/content/glava-7-sozdanie-internet-magazina/sozdanie-korzini/registratsiya-zakazov/sozdanie-zakazov-klientov.html