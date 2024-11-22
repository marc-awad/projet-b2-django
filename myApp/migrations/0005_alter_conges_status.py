# Generated by Django 5.1.3 on 2024-11-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_conges_validate_conges_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conges',
            name='status',
            field=models.CharField(choices=[('en_attente', 'En attente'), ('refusee', 'Refusée'), ('validee', 'Validée')], default='en_attente', max_length=10),
        ),
    ]
