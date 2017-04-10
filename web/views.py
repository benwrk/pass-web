from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from PASSweb import settings
import json
from django.http.response import HttpResponseRedirect

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
    
    floor_filters = None
    group_filters = None
    ward_filters = None
    
    if floors:
        floor_filters = str(floors).lower().replace('+', ' ').split(',')
    if groups:
        group_filters = str(groups).lower().replace('+', ' ').split(',')
    if wards:
        ward_filters = str(wards).lower().replace('+', ' ').split(',')
    
    for floor in groupings['floors']:
        floor['selected'] = not floor_filters or floor['name'].lower() in floor_filters
        for group in floor['groups']:
            group['selected'] = not group_filters or (floor['name'] + ' - ' + group['name']).lower() in group_filters
            for ward in group['wards']:
                ward['selected'] = not ward_filters or (floor['name'] + ' - ' + group['name'] + ' - ' + ward['name']).lower() in ward_filters

def get_boxes_from_groupings(groupings):
    boxes = []
    for floor in [value for value in groupings['floors'] if value['selected']]:
        for group in [value for value in floor['groups'] if value['selected']]:
            for ward in [value for value in group['wards'] if value['selected']]:
                for box in ward['boxes']:
                    boxes.append(box)
    return boxes

def send_selective(request):
    """Renders the selective send page."""
    assert isinstance(request, HttpRequest)
    groupings = read_grouping_config()
    process_filters(groupings, request.GET.get('floors'), request.GET.get('groups'), request.GET.get('wards'))
    if request.method == 'GET':
        return render(request, 'blocks/send_selective.html', { 
            'boxes': get_boxes_from_groupings(groupings),
            'groupings_json': json.dumps(groupings),
            'groupings': groupings,
            'nav': 'selective',
            'step': int(request.GET.get('step', '1')),
            'layout': {
                'active_nav': 'Selective',
                'page_name': 'Selective'
            }
         })

def send_direct(request):
    """Renders the send page. """
    return HttpResponse(404);

def send_broadcast(request):
    return HttpResponse(404);
    