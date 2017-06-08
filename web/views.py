from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseRedirect
from django.utils.http import urlencode
from web.mapping_server import MappingServer
from PASSweb import settings
import json
import socket

mapper = MappingServer(settings.CONFIGS.get('client_broadcasting_port', 1256), settings.CONFIGS.get('max_udp_size', 1024))
mapper.run()
client_listening_port = settings.CONFIGS.get('client_listening_port', 1257)

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

def get_boxes_from_groupings(groupings, addresses=None):
    boxes = []
    for floor in [value for value in groupings['floors'] if not 'selected' in value or value['selected']]:
        for group in [value for value in floor['groups'] if not 'selected' in value or value['selected']]:
            for ward in [value for value in group['wards'] if not 'selected' in value or  value['selected']]:
                for box in [value for value in ward['boxes'] if not addresses or value['address'].lower() in addresses]:
                    box['floor_name'] = floor['name']
                    box['group_name'] = group['name']
                    box['ward_name'] = ward['name']
                    boxes.append(box)
    return boxes

def send_selective(request):
    """Renders the selective send page."""
    assert isinstance(request, HttpRequest)
    groupings = read_grouping_config()
    process_filters(groupings, request.GET.get('floors'), request.GET.get('groups'), request.GET.get('wards'))
    if request.method == 'GET':
        return render(request, 'blocks/send_selective.html', { 
            'boxes': get_boxes_from_groupings(groupings, request.GET.get('boxes', '').lower().split(',')) if 'boxes' in request.GET else None,
            'groupings': groupings,
            'nav': 'selective',
            'step': int(request.GET.get('step', '1')),
            'layout': {
                'active_nav': 'Selective',
                'page_name': 'Selective'
            }
         })

def send_direct(request):
    """Renders the direct send page."""
    assert isinstance(request, HttpRequest)
    

def send_broadcast(request):    
    """Renders the broadcast page."""
    groupings = read_grouping_config()
    
    if request.method == 'GET':
        return render(request, 'blocks/send.html', { 
            'boxes': get_boxes_from_groupings(groupings),
            'layout': {
                'active_nav': 'Broadcast',
                'page_name': 'Broadcast',
                'extra_title': 'Broadcast Message',
                'send_success': bool(int(request.GET.get('success', '0')))
            }
         })


def send(request):
    """Renders the send page."""
    assert isinstance(request, HttpRequest)
    groupings = read_grouping_config()

    if request.method == 'GET':
        return render(request, 'blocks/send.html', { 
            'boxes': get_boxes_from_groupings(groupings, request.GET.get('boxes', '').lower().split(',')) if 'boxes' in request.GET else None,
            'layout': {
                'active_nav': 'Send',
                'page_name': 'Send',
                'extra_title': 'Message'
            }
         })

def send_service_call(request):
    assert isinstance(request, HttpRequest)
    
    if request.is_ajax() and request.method == 'POST':
        body = request.body
        decoded_body = body.decode('utf-8')
        json_body = json.loads(decoded_body)

        # Python 3.0 - 3.5 Windows Console Bug! Need to parse and re-encode!
        # print(str(json_body).encode('utf-8'))

        message = json_body['message']
        display = json_body['messageOptions']['display']
        duration = json_body['messageOptions']['duration'] if display.lower() == 'toast' else None

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for box in json_body['addresses']:
            if box in mapper.mac_ip_map:
                sock.sendto(b'PASS_MSG/!!/' + bytes(display.upper(), 'utf-8') + b'/!!/' + bytes(message, 'utf-8') + b'/!!/' + bytes(str(duration) if duration else '0', 'utf-8'), (mapper.mac_ip_map.get(box), client_listening_port))
               
        return HttpResponse("OK")


#def home(request):
#    assert isinstance(request, HttpRequest)
#    return HttpResponseRedirect('/send_broadcast' + (('?' + urlencode(params)) if params else ''))
