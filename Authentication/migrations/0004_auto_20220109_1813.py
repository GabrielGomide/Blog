# Generated by Django 3.1.6 on 2022-01-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_auto_20220109_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='can_post',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
