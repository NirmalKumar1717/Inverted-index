# Generated by Django 2.2.7 on 2019-11-22 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0006_auto_20191122_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='words',
        ),
    ]