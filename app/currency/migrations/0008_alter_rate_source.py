# Generated by Django 4.1.7 on 2023-03-24 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_requestresponselog_alter_rate_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.source'),
        ),
    ]