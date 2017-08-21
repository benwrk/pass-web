import argparse
import json
import os
from django.core.management import execute_from_command_line
from django.core.management.base import BaseCommand
from service_app.models import Floor, Group, Box, Ward

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print('[StartService] BASE_DIR = \'' + BASE_DIR + '\'')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--config', type=argparse.FileType('r'), default=os.path.join(BASE_DIR, 'configs/app.json'))

    def handle(self, *args, **options):
        with (options['config']) as config_file:
            print('[StartService] Using app config from ' + config_file.name)
            print('[StartService] Loading configurations...')
            config = json.load(config_file)
            print('[ConfigLoad] ' + json.dumps(config))

            execute_from_command_line(['manage.py', 'load_address_config', os.path.join(BASE_DIR, config['address_config_file'])])
            execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:' + config['port']])

