from rest_framework import serializers
from service_app.models import Floor, Group, Ward, Box


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

    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(required=True)
    ##groups = GroupSerializer(many=True)

    #def create(self, validated_data):
    #    return Floor.objects.create(**validated_data)

    #def update(self, instance, validated_data):
    #    instance.name = validated_data.get('name', instance.name)
    #    instance.save()
    #    return instance
