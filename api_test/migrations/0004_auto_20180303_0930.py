# Generated by Django 2.0.2 on 2018-03-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=11, verbose_name='手机号'),
        ),
    ]