# Generated by Django 2.2.2 on 2019-06-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rememorize_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memcard',
            name='show_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'random'), (1, 'show_key'), (2, 'show_value')], default=0, help_text='카드 유형'),
        ),
    ]
