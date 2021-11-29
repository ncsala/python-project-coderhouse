# Generated by Django 3.2.9 on 2021-11-29 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_remove_department_anulate'),
        ('employees', '0004_remove_employee_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.department'),
            preserve_default=False,
        ),
    ]