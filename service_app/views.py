from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from service_app.models import Floor, Group, Ward, Box
from service_app.serializers import FloorSerializer

@csrf_exempt
def floor_list(request):
    if request.method == 'GET':
        floors = Floor.objects.all()
        serializer = FloorSerializer(floor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FloorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def floor_detail(request, pk):
    try:
        floor = Floor.objects.get(pk=pk)
    except Floor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FloorSerializer(floor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FloorSerializer(floor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        floor.delete()
        return HttpResponse(status=204)
