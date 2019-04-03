from django.contrib import admin
from api.models import Item,Cart,Order

# Register your models here.
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Order)