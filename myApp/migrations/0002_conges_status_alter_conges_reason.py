# Generated by Django 5.1.3 on 2024-11-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conges',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conges',
            name='reason',
            field=models.CharField(choices=[('conges_payes', 'Congés Payés'), ('conges_maladie', 'Congés Maladie'), ('conges_exceptionnels', 'Congés Exceptionnels')], default='conges_payes', max_length=20),
        ),
    ]
