# Generated by Django 4.0 on 2022-01-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_businesshourday_horaabre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading',
            name='negocioRubro',
            field=models.ManyToManyField(through='polls.BusinessArea', to='polls.Business'),
        ),
    ]