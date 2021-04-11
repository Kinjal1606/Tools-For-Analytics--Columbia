import csv
from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from dateutil import parser
from datetime import datetime

class Command(BaseCommand):
    help=('Import squirrel data from csv file into our Database')
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)
        
    def handle(self,*args,**kwargs):
        path = kwargs['path']

        try:
            with open(path,encoding='utf-8') as fn:
                reader = csv.DictReader(fn)
                for r in reader:
                    sight = Squirrel(
                        lat=r['Y'],
                        lon=r['X'],
                        unique_id=r['Unique Squirrel ID'],
                        shift=r['Shift'],
                        date=datetime.strptime(r['Date'], r'%m%d%Y'),
                        age=r['Age'],
                        fur_color=r['Primary Fur Color'],
                        location = r['Location'],
                        specific_loc = r['Specific Location'],
                        running=(r['Running']=='true'),
                        chasing=(r['Chasing']=='true'),
                        climbing=(r['Climbing']=='true'),
                        eating=(r['Eating']=='true'),
                        foraging=(r['Foraging']=='true'),
                        other_activities=r['Other Activities'],
                        kuks=(r['Kuks']=='true'),
                        quaas=(r['Quaas']=='true'),
                        moans=(r['Moans']=='true'),
                        tail_flags=(r['Tail flags']=='true'),
                        tail_twitches=(r['Tail twitches']=='true'),
                        approaches=(r['Approaches']=='true'),
                        #indifferent=r['Indifferent'].upper(),
                        runs_from=(r['Runs from']=='true'),
                        )
                    sight.save()
        except csv.Error as e:
            print(f'Error with {reader.line_num}')

