# Generated by Django 2.1.2 on 2020-04-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_number',
            field=models.IntegerField(default=1),
        ),
    ]
