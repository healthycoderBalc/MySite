# Generated by Django 4.0 on 2022-01-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_client_fechanacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='fechaNacimiento',
            field=models.DateTimeField(verbose_name='Fecha de Nacimiento'),
        ),
    ]