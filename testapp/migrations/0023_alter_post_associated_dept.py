# Generated by Django 3.2.15 on 2022-12-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0022_remove_post_sell_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='associated_dept',
            field=models.CharField(max_length=50),
        ),
    ]