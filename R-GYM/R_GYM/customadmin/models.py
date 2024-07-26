from django.db import models

# Create your models here.
class admin_category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    cat_image = models.FileField(upload_to="category/", max_length=50, null=True, default=None)
    def __str__(self):
        return self.cat_name

class admin_product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_price = models.FloatField(max_length=20)
    product_quantity = models.CharField(max_length=20)
    product_tag = models.CharField(max_length=50)
    product_image = models.FileField(upload_to="product/", max_length=50, null=True, default=None)
    product_short_description = models.TextField()
    product_information = models.TextField()
    product_description = models.TextField()
    def __str__(self):
        return self.product_name

class admin_package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=50)
    package_duration = models.CharField(max_length=20)
    package_price = models.CharField(max_length=20)
    package_image = models.FileField(upload_to="package/", max_length=50, null=True, default=None)
    package_specification = models.TextField()
    package_description = models.TextField()
    def __str__(self):
        return self.package_name

class admin_trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=50)
    trainer_type = models.CharField(max_length=50)
    trainer_speciality = models.CharField(max_length=50)
    trainer_image = models.FileField(upload_to="trainer/", max_length=50, null=True, default=None)
    trainer_description = models.TextField()
    def __str__(self):
        return self.trainer_name

class admin_class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    class_title = models.CharField(max_length=50)
    class_description = models.TextField()
    class_benefits = models.TextField()
    class_image = models.FileField(upload_to="class/", max_length=50, null=True, default=None)
    def __str__(self):
        return self.class_name

class admin_timetable(models.Model):
    timetable_id = models.AutoField(primary_key=True)
    timetable_class = models.CharField(admin_class, max_length=20)
    timetable_day = models.CharField(max_length=20)
    timetable_starttime = models.TimeField(max_length=20)
    timetable_endtime = models.TimeField(max_length=20)