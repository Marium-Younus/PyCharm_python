from django.contrib import admin
from .models import order

class product_order(admin.ModelAdmin):
    list_display = ['order_id', 'user_name', 'user_country', 'user_address', 'user_zip', 'user_phone', 'user_email', 'product_id', 'product_name', 'total_price', 'order_status']

admin.site.register(order, product_order)