# Generated by Django 4.2.3 on 2023-07-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0005_admin_package_rename_category_admin_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_name', models.CharField(max_length=50)),
                ('trainer_type', models.CharField(max_length=50)),
                ('trainer_speciality', models.CharField(max_length=50)),
                ('trainer_image', models.CharField(max_length=20)),
                ('trainer_description', models.TextField()),
            ],
        ),
    ]