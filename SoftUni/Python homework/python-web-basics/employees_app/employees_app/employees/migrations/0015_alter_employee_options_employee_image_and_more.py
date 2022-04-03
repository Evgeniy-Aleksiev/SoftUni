# Generated by Django 4.0.2 on 2022-02-11 11:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('company', '-first_name')},
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.CharField(choices=[('SoftUni', 'SoftUni'), ('Google', 'Google'), ('Facebook', 'Facebook'), ('AUDI', 'AUDI')], max_length=8),
        ),
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='EGN'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'DevOps Specialist')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='dead_line',
            field=models.DateField(blank=True, null=True),
        ),
    ]