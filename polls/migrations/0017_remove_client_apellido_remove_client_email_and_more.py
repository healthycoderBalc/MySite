# Generated by Django 4.0 on 2022-01-28 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('polls', '0016_contactform_logo_alter_business_fotologotipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='client',
            name='nombre',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]