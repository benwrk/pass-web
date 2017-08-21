from rest_framework import serializers
from service_app.models import Floor, Group, Ward, Box, Message


class BoxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'

class WardSerializer(serializers.HyperlinkedModelSerializer):
    boxes = BoxSerializer(many=True)
    class Meta:
        model = Ward
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    wards = WardSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'

class FloorSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = Floor
        fields = '__all__'

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
