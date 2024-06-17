# Generated by Django 4.2.4 on 2023-09-02 22:37

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0017_videocall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='members',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='videocall',
            name='date_ended',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 2, 7, 9, 292908)),
        ),
        migrations.AlterField(
            model_name='videocall',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 3, 2, 7, 9, 292899)),
        ),
    ]
