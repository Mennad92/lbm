from django.contrib import admin
from biscuits.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserData)
admin.site.register(Order)
admin.site.register(OrderElement)