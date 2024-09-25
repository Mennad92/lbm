from django.contrib import admin
from biscuits.models import *
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from db_file_storage.form_widgets import DBAdminClearableFileInput

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        widgets = {
            'picture': DBAdminClearableFileInput
        }

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'get_visit_count')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    filter_horizontal = ('ingredients',)
    form = ProductForm

    def get_visit_count(self, obj):        
        try:
            product_data = ProductData.objects.using("djongo").get(product_id=obj.id)
            visit_count = product_data.visit_count
        except ObjectDoesNotExist:
            visit_count = 0
        
        return visit_count

    get_visit_count.short_description = 'Nombre de visites'

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserData)
admin.site.register(Order)
admin.site.register(OrderElement)
admin.site.register(Ingredient)