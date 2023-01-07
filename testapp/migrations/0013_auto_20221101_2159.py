# Generated by Django 3.2.15 on 2022-11-01 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0012_auto_20221031_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='associated_dept',
            field=models.CharField(choices=[('BME', 'Biomedical Engineering'), ('CHE', 'Chemical Engineering'), ('CS', 'Computer Science'), ('ECE', 'Electrical and Computer Engineering'), ('STS', 'Engineering and Society'), ('MSE', 'Material Sciences Engineering'), ('MAE', 'Mechanical and Aerospace Engineering'), ('SYS', 'Systems Engineering'), ('CE', 'Civil Engineering'), ('APMA', 'Applied Mathematics')], default='CS', max_length=4),
        ),
    ]