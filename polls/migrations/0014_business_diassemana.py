# Generated by Django 4.0 on 2022-01-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_business_formascontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='diasSemana',
            field=models.ManyToManyField(through='polls.Businesshourday', to='polls.Dayweek'),
        ),
    ]