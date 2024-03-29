# Generated by Django 4.1.7 on 2023-03-28 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_alter_rate_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.source'),
        ),
    ]
