# Generated by Django 2.2 on 2019-05-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmachart', '0008_auto_20190521_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='create_datetime',
            field=models.TextField(blank=True, null=True),
        ),
    ]
