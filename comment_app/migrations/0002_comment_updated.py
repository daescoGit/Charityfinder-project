# Generated by Django 2.2 on 2020-05-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]