# Generated by Django 4.1.7 on 2023-04-06 13:48

import currency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0009_source_logo_alter_rate_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='sell',
            new_name='sale',
        ),
        migrations.AlterField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=True, null=True, upload_to=currency.models.source_logo_path),
        ),
    ]
