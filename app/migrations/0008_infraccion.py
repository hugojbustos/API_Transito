# Generated by Django 5.0.1 on 2024-02-02 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_infraccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_patente', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('comentarios', models.TextField()),
                ('oficial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.policia')),
            ],
        ),
    ]
