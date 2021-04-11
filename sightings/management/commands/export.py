from django.core.management.base import BaseCommand

import csv

from tracker.models import Sighting

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        dict_ = {} 
        s = Sighting.objects.all()
        with open(options['csv_file'],"w") as fp:
            for i in s:
                dict_['Longitude'] = i.lon
                dict_['Latitude'] = i.lat
                dict_['Shift'] = i.shift
                dict_['Date'] = i.date
                dict_['Unique Squirrel ID'] = i.unique_id
                dict_['Age'] = i.age
                dict_['Primary Fur Color'] = i.fur_color
                dict_['Location'] = i.location
                dict_['Specific Location'] = i.specific_loc
                dict_['Running'] = i.running
                dict_['Chasing'] = i.chasing
                dict_['Climbing'] = i.climbing
                dict_['Eating'] = i.eating
                dict_['Foraging'] = i.foraging
                dict_['Other Activities'] = i.other_activities
                dict_['Kuks'] = i.kuks
                dict_['Quaas'] = i.quaas
                dict_['Moans'] = i.moans
                dict_['Tail Flags'] = i.tail_flags
                dict_['Tail Twitches'] = i.tail_twitches
                dict_['Approaches'] = i.approaches
                dict_['Runs from'] = i.runs_from
                writer = csv.DictWriter(fp,delimiter=",",fieldnames=dict_.keys())
                writer.writeheader()
                writer.writerow(dict_)
