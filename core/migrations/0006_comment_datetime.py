# Generated by Django 3.1.6 on 2022-01-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220112_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]