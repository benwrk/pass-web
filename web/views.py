from django.shortcuts import render
from django.http import HttpRequest
from PASSweb import settings
import json

def read_grouping_config():
    groupings = {}
    try:
        if settings.CONFIGS:
            GROUPING_CONFIG = settings.CONFIGS.get('grouping-config', 'grouping.json') 
            with open(settings.CONFIGS.get('grouping-config', 'grouping.json')) as grouping_config:
                groupings = json.load(grouping_config)
    except IOError:
        print('[IOError] Cannot read or find the grouping configuration file!')
        raise IOError('[IOError] Cannot read or find the grouping configuration file!')
    return groupings

def send(request):
    """Renders the send page."""
    assert isinstance(request, HttpRequest)
    
    #read_grouping_config()
    
    return render(request, 'index.html', { 'content': read_grouping_config() })
    