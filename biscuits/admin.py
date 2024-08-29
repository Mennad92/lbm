from django.contrib import admin
from biscuits.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    filter_horizontal = ('ingredients',) 
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserData)
admin.site.register(Order)
admin.site.register(OrderElement)
admin.site.register(Ingredient)