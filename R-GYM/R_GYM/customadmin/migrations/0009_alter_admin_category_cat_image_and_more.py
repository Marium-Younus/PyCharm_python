# Generated by Django 4.2.3 on 2023-07-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0008_admin_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_category',
            name='cat_image',
            field=models.FileField(default=None, max_length=50, null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='admin_package',
            name='package_image',
            field=models.FileField(default=None, max_length=50, null=True, upload_to='package/'),
        ),
        migrations.AlterField(
            model_name='admin_product',
            name='product_image',
            field=models.FileField(default=None, max_length=50, null=True, upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='admin_trainer',
            name='trainer_image',
            field=models.FileField(default=None, max_length=50, null=True, upload_to='trainer/'),
        ),
    ]
