# Generated by Django 3.0.6 on 2020-05-29 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_auto_20200528_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.TextField(default='no-name')),
                ('Event_Start_Date', models.DateField(default='2020-00-00')),
                ('Event_Start_Time', models.TimeField(default='00:00:00')),
                ('Event_End_Date', models.DateField(default='2020-00-00')),
                ('Event_End_Time', models.TimeField(default='00:00:00')),
                ('Event_Description', models.TextField(default='Opis')),
                ('Event_Program', models.TextField(default='Program')),
                ('Even_Owner', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SmallEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Show_Name', models.TextField(default='no-name')),
                ('Show_Start_Date', models.DateField(default='2020-00-00')),
                ('Show_Start_Time', models.TimeField(default='00:00:00')),
                ('Show_End_Date', models.DateField(default='2020-00-00')),
                ('Show_End_Time', models.TimeField(default='00:00:00')),
                ('Show_Description', models.TextField(default='Opis')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
