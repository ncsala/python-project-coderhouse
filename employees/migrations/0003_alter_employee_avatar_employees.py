# Generated by Django 3.2.9 on 2021-12-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_avatar_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar_employees',
            field=models.ImageField(blank=True, null=True, upload_to='employees'),
        ),
    ]