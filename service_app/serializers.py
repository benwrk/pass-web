from rest_framework import serializers
from service_app.models import Floor, Group, Ward, Box

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('id', 'name')
    #id = serializers.IntegerField(read_only=True)
    #name = serializers.CharField(required=True)
    ##groups = GroupSerializer(many=True)

    #def create(self, validated_data):
    #    return Floor.objects.create(**validated_data)

    #def update(self, instance, validated_data):
    #    instance.name = validated_data.get('name', instance.name)
    #    instance.save()
    #    return instance
