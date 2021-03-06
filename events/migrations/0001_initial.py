# Generated by Django 3.0.6 on 2020-05-28 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.TextField(default='no-name')),
                ('Event_Start_Date', models.DateField(default='0000-00-00')),
                ('Event_Start_Time', models.TimeField(default='00:00:00')),
                ('Event_End_Date', models.DateField(default='0000-00-00')),
                ('Event_End_Time', models.TimeField(default='00:00:00')),
                ('Even_Owner', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
