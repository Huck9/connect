# Generated by Django 3.0.6 on 2020-05-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Even_Owner',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]