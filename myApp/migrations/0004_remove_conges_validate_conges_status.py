# Generated by Django 5.1.3 on 2024-11-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_rename_status_conges_validate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conges',
            name='validate',
        ),
        migrations.AddField(
            model_name='conges',
            name='status',
            field=models.CharField(default='en_attente', max_length=10),
        ),
    ]
