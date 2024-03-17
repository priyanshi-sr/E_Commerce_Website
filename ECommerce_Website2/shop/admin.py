from django.contrib import admin

# Register your models here.
from .models import Product, OrderUpdate
from .models import Contact
from .models import Orders

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
