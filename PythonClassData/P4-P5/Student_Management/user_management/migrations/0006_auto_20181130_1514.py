# Generated by Django 2.1.1 on 2018-11-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_auto_20181130_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rollnumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
