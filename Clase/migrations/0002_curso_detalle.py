# Generated by Django 5.0.6 on 2024-05-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='detalle',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
