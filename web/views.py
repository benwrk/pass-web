from django.shortcuts import render
from django.http import HttpRequest
from PASSweb import settings
import json
from django.http.response import HttpResponse

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

def process_filters(groupings, floors=None, groups=None, wards=None):
    filtered_groupings = dict(groupings)

    if floors:
        floor_filters = str(floors).lower().split(',')
        filtered_groupings['floors'][:] = [value for value in filtered_groupings['floors'] if str(value['name']).lower() in floor_filters]
    
    group_filters = None
    ward_filters = None

    if groups or wards:
        if groups:
            group_filters = str(groups).lower().split(',')
        if wards:
            ward_filters = str(wards).lower().split(',')
        for floor in filtered_groupings['floors']:
            if groups:
                floor['groups'][:] = [value for value in floor['groups'] if str(value['name']).lower() in group_filters]
            if wards:
                for group in floor['groups']:
                    group['wards'][:] = [value for value in group['wards'] if str(value['name']).lower() in ward_filters]
    
    filtered_groupings['filtered'] = True
    return filtered_groupings

def send(request):
    """Renders the send page."""
    assert isinstance(request, HttpRequest)
    
    if request.method == 'GET':
        groupings = process_filters(read_grouping_config(), request.GET['floors'], request.GET['groups'], request.GET['wards'])
        return render(request, 'index.html', { 'content': groupings })
    elif request.method == 'POST':
        return HttpResponse(status=404)

    