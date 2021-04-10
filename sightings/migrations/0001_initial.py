# Generated by Django 3.1.7 on 2021-04-10 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('lat', models.FloatField(blank=True, help_text='Latitude (Y) of the sighting')),
                ('lon', models.FloatField(blank=True, help_text='Longitude (X) of the sighting')),
                ('unique_id', models.CharField(default=None, help_text='Unique squirrel ID', max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)])),
                ('shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift of sighting', max_length=100)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='age of squirrel', max_length=100)),
                ('fur_color', models.CharField(blank=True, choices=[('Grey', 'Grey'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='squirrel fur color', max_length=30)),
                ('location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='location of squirrel sighting', max_length=100)),
                ('specific_loc', models.CharField(blank=True, help_text='specific location', max_length=100)),
                ('running', models.BooleanField(default=False, help_text='Whether it is Running')),
                ('chasing', models.BooleanField(default=False, help_text='whether it is chasing')),
                ('climbing', models.BooleanField(default=False, help_text='whether it is climbing')),
                ('eating', models.BooleanField(default=False, help_text='whether it is eating')),
                ('foraging', models.BooleanField(default=False, help_text='Foraging')),
                ('other_activities', models.CharField(blank=True, help_text='other activity of squirrel', max_length=100)),
                ('kuks', models.BooleanField(default=False, help_text='Kuks')),
                ('quaas', models.BooleanField(default=False, help_text='quaas')),
                ('moans', models.BooleanField(default=False, help_text='moans')),
                ('tail_flags', models.BooleanField(default=False, help_text='tail flags')),
                ('tail_twitches', models.BooleanField(default=False, help_text='tail twitches')),
                ('approaches', models.CharField(default=False, help_text='approaches', max_length=100)),
                ('runs_from', models.BooleanField(default=False, help_text='runs from')),
            ],
        ),
    ]
