import argparse
import json
from django.core.management.base import BaseCommand
from service_app.models import Floor, Group, Box, Ward

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        print('[Management] Clearing address configs from DB...')
        Floor.objects.all().delete()
        Group.objects.all().delete()
        Ward.objects.all().delete()
        Box.objects.all().delete()

        with (options['file']) as config_file:
            print('[Management] Loading address configs from ' + config_file.name)
            config_json = json.load(config_file)
            for floor in config_json['floors']:
                f = Floor(name=floor['name'])
                f.save()
                for group in floor['groups']:
                    g = Group(name=group['name'], floor=f)
                    g.save()
                    for ward in group['wards']:
                        w = Ward(name=ward['name'], group=g)
                        w.save()
                        for box in ward['boxes']:
                            b = Box(name=box['name'], mac_address=box['mac_address'], ward=w)
                            b.save()

            print('[Management] Finished loading config file ' + config_file.name)

                    
