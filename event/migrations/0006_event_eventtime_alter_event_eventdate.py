# Generated by Django 4.0.3 on 2022-05-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_attend_education_alter_attend_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventDate',
            field=models.DateField(null=True),
        ),
    ]
