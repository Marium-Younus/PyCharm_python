from django.contrib import admin
from .models import admin_category, admin_product, admin_package, admin_trainer, admin_class, admin_timetable
# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display = ['cat_id', 'cat_name', 'cat_image']

class product_admin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_category', 'product_price', 'product_quantity', 'product_tag', 'product_image', 'product_short_description', 'product_information', 'product_description']

class package_admin(admin.ModelAdmin):
    list_display = ['package_id', 'package_name', 'package_duration', 'package_price', 'package_image', 'package_specification', 'package_description']

class trainer_admin(admin.ModelAdmin):
    list_display = ['trainer_id', 'trainer_name', 'trainer_type', 'trainer_speciality', 'trainer_image', 'trainer_description']

class class_admin(admin.ModelAdmin):
    list_display = ['class_id', 'class_name', 'class_title', 'class_description', 'class_benefits', 'class_image']

class timetable_admin(admin.ModelAdmin):
    list_display = ['timetable_id', 'timetable_class', 'timetable_day', 'timetable_starttime', 'timetable_endtime']

admin.site.register(admin_category, category_admin)
admin.site.register(admin_product, product_admin)
admin.site.register(admin_package, package_admin)
admin.site.register(admin_trainer, trainer_admin)
admin.site.register(admin_class, class_admin)
admin.site.register(admin_timetable, timetable_admin)