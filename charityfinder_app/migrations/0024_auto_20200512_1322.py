# Generated by Django 2.2 on 2020-05-12 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityfinder_app', '0023_auto_20200512_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=models.SET(8), to=settings.AUTH_USER_MODEL),
        ),
    ]
