# Generated by Django 2.1.3 on 2018-11-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20181128_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationtype',
            name='monthlyComitment',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
