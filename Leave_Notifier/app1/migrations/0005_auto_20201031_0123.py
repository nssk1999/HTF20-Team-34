# Generated by Django 3.0.5 on 2020-10-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_facultydetails_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultydetails',
            name='dept',
            field=models.CharField(max_length=40),
        ),
    ]
