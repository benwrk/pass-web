from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from service_app.models import Floor, Group, Ward, Box
from service_app.serializers import FloorSerializer

@api_view(['GET', 'POST'])
def floor_list(request, format=None):
    if request.method == 'GET':
        floors = Floor.objects.all()
        serializer = FloorSerializer(floors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def floor_detail(request, pk, format=None):
    try:
        floor = Floor.objects.get(pk=pk)
    except Floor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FloorSerializer(floor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FloorSerializer(floor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        floor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
