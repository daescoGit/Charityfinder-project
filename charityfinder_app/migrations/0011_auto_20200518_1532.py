# Generated by Django 2.2 on 2020-05-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charityfinder_app', '0010_auto_20200518_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment',
            new_name='comment_id',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='parent',
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_to_id',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]
