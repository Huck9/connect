# Generated by Django 3.0.6 on 2020-05-30 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0017_eventopinion_user_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='smallEventOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opinion', models.TextField(max_length=250)),
                ('Name', models.TextField(default='User', max_length=100)),
                ('SmallEvent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.SmallEvent')),
                ('User_Add', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
