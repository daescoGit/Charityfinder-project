# Generated by Django 2.2 on 2020-05-12 10:16

import charityfinder_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charityfinder_app', '0018_auto_20200511_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['up_votes', 'created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=models.SET(charityfinder_app.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='charityfinder_app.Comment'),
        ),
    ]
