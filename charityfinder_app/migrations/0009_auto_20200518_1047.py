# Generated by Django 2.2 on 2020-05-18 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charityfinder_app', '0008_auto_20200516_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_comment', to='charityfinder_app.Comment')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parent_comment', to='charityfinder_app.Comment')),
            ],
        ),
    ]
