# Generated by Django 2.1.4 on 2019-01-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_group_edit_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='edit_history',
            field=models.TextField(default='[]'),
        ),
    ]
