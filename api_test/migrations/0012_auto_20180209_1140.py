# Generated by Django 2.0.2 on 2018-02-09 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0011_auto_20180209_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_number', to='api_test.Project', verbose_name='所属项目'),
        ),
    ]