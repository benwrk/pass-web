from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from service_app.models import Floor, Group, Ward, Box
from service_app.serializers import FloorSerializer, GroupSerializer, WardSerializer, BoxSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'floors': reverse('floor-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'wards': reverse('ward-list', request=request, format=format),
        'boxes': reverse('box-list', request=request, format=format)
    })

class FloorList(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class FloorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class WardList(generics.ListCreateAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class WardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer

class BoxList(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

#from service_app.models import Floor
#from service_app.serializers import FloorSerializer
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

#class FloorList(APIView):
#    def get(self, request, format=None):
#        floors = Floor.objects.all()
#        serializer = FloorSerializer(floors, many=True)
#        return Response(serializer.data)

#    def post(self, request, format=None):
#        serializer = FloorSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class FloorDetail(APIView):
#    def get_object(self, pk):
#        try:
#            return Floor.objects.get(pk=pk)
#        except Snippet.DoesNotExist:
#            raise Http404

#    def get(self, request, pk, format=None):
#        floor = self.get_object(pk)
#        serializer = FloorSerializer(floor)
#        return Response(serializer.data)

#    def put(self, request, pk, format=None):
#        floor = self.get_object(pk)
#        serializer = FloorSerializer(floor, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
#        floor = self.get_object(pk)
#        floor.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
