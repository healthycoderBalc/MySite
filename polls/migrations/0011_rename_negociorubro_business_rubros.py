# Generated by Django 4.0 on 2022-01-19 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_heading_negociorubro_business_negociorubro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='negocioRubro',
            new_name='Rubros',
        ),
    ]