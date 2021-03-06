# Generated by Django 3.0.5 on 2020-10-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date_of_leave', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('reason', models.TextField(default='')),
                ('permission', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
