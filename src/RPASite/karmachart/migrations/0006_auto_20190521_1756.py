# Generated by Django 2.2 on 2019-05-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmachart', '0005_auto_20190520_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='codyexample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codysname', models.TextField(blank=True, db_column='codysname', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='submissiondata',
            name='number_48_hour',
            field=models.TextField(blank=True, db_column='48_hour', null=True),
        ),
    ]
