# Generated by Django 3.1.7 on 2021-04-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20210412_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age of squirrel', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.CharField(default=False, help_text='Approaches', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(default=False, help_text='Whether it is chasing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(default=False, help_text='Whether it is climbing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(default=False, help_text='Whether it is eating'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(default=False, help_text='Foraging'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='fur_color',
            field=models.CharField(blank=True, choices=[('Grey', 'Grey'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Squirrel fur color', max_length=30),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location of squirrel sighting', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(default=False, help_text='Moans'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(blank=True, help_text='Other activity of squirrel', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(default=False, help_text='Quaas'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(default=False, help_text='Whether it is Running'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(default=False, help_text='Runs from'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='specific_loc',
            field=models.CharField(blank=True, help_text='Specific location', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default=False, help_text='Tail flags'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(default=False, help_text='Tail twitches'),
        ),
    ]
