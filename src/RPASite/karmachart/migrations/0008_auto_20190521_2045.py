# Generated by Django 2.2 on 2019-05-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmachart', '0007_delete_codyexample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissions',
            name='id',
        ),
        migrations.AlterField(
            model_name='submissions',
            name='submissionid',
            field=models.TextField(db_column='SubmissionID', primary_key=True, serialize=False),
        ),
    ]