# Generated by Django 2.1.2 on 2020-05-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_plan_plan_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('banner_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
