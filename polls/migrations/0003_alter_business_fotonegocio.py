# Generated by Django 4.0 on 2022-01-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choice_businesscontactform_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='fotoNegocio',
            field=models.ImageField(upload_to='images/'),
        ),
    ]