# Generated by Django 2.1.3 on 2018-11-28 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20181127_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='donationtMade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.donationtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]
