# Generated by Django 4.1.7 on 2023-02-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_create_model_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]