# Generated by Django 3.2.9 on 2021-12-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar_employees',
            field=models.ImageField(blank=True, null=True, upload_to='employee'),
        ),
    ]
