from rest_framework import serializers
from service_app.models import Floor, Group, Ward, Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    boxes = BoxSerializer(many=True)
    class Meta:
        model = Ward
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    wards = WardSerializer(many=True)
    class Meta:
        model = Group
        fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
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
