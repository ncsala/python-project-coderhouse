# Generated by Django 3.2.9 on 2021-11-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20211128_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='numero',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]