# Generated by Django 4.2.3 on 2023-08-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0012_alter_admin_timetable_timetable_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_class',
            name='class_benefits',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='admin_class',
            name='class_description',
            field=models.TextField(),
        ),
    ]
