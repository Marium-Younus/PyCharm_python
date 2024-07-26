from django.db import models

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_country = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    user_zip = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    total_price = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    def __str__(self):
        return self.user_name