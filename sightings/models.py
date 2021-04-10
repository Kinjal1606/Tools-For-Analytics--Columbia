from django.db import models
from django.utils.translation import gettext as _

from django.core.validators import MinLengthValidator

class Squirrel(models.Model):
    lat = models.FloatField(
        help_text=_('Latitude (Y) of the sighting'),
        blank = True,
        )
    lon = models.FloatField(
            help_text=_('Longitude (X) of the sighting'),
            blank = True,
            )

    unique_id= models.CharField(
         max_length=100,
         validators=[MinLengthValidator(10)],
         help_text=_('Unique squirrel ID'),
         primary_key= True,
         default=None,
         )

    AM='AM'
    PM='PM'
    shift_choices = ((AM,'AM'),(PM,'PM'))
    shift = models.CharField(
            max_length = 100,
            choices = shift_choices,
            help_text = _('Shift of sighting'),
            blank = True
            )
    date = models.DateField(
            help_text = _('Date'),
            )
    ADULT='Adult'
    JUVENILE = 'Juvenile'
    age_choices = ((ADULT,'Adult'), (JUVENILE,'Juvenile'))

    age = models.CharField(
            max_length=100,
            choices = age_choices, 
            help_text=_('age of squirrel'),
            blank = True,
            )
    GREY= 'Grey'
    CINNAMON= 'Cinnamon'
    BLACK = 'Black'
    color_choices = ((GREY,'Grey'),(CINNAMON, 'Cinnamon'),(BLACK,'Black'))
    fur_color = models.CharField(
            max_length=30,
            choices= color_choices,
            help_text=_('squirrel fur color'),
            blank=True,
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    location_choices = ((GROUND_PLANE,'Ground Plane'), (ABOVE_GROUND, 'Above Ground'))
    location = models.CharField(
            max_length=100,
            choices = location_choices,
            help_text=_('location of squirrel sighting'),
            blank = True,
            )
    specific_loc = models.CharField(
            max_length=100,
            blank=True,
            help_text=_('specific location'),
         )
    running = models.BooleanField(
            help_text=_('Whether it is Running'),
            default = False,
            )
    chasing = models.BooleanField(
            help_text=_('whether it is chasing'),
            default = False,
            )
    climbing= models.BooleanField(
            help_text=_('whether it is climbing'),
            default = False,
            )
    eating= models.BooleanField(
            help_text=_('whether it is eating'),
            default = False,
            )
    foraging= models.BooleanField(
            help_text=_('Foraging'),
            default = False,
            )
    other_activities= models.CharField(
            max_length=100,
            blank=True,
            help_text=_('other activity of squirrel')
           )
    kuks= models.BooleanField(
            help_text=_('Kuks'),
            default = False,
            )
    quaas= models.BooleanField(
            help_text=_('quaas'),
            default = False,
            )
    moans= models.BooleanField(
            help_text=_('moans'),
            default = False,
            )
    tail_flags = models.BooleanField(
            help_text=_('tail flags'),
            default = False,
            )
    tail_twitches= models.BooleanField(
            help_text=_('tail twitches'),
            default = False,
            )
    approaches = models.CharField(
            max_length=100,
            help_text=_('approaches'),
            default = False,
            )
    runs_from= models.BooleanField(
            help_text=_('runs from'),
            default = False,
            )
