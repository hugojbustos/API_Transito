# Generated by Django 5.0.1 on 2024-02-02 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_infraccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infraccion',
            name='oficial',
        ),
    ]
