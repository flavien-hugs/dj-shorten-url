# Generated by Django 3.0.6 on 2020-05-22 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortenURL', '0002_shorten_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorten',
            name='slug',
        ),
    ]
