# Generated by Django 2.1.3 on 2018-11-27 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20181126_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]
