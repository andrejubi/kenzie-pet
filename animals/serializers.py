from rest_framework import serializers
from groups.serializers import GroupSerializer
from features.serializers import FeatureSerializer
from .models import Animal
from helpers.animal_helpers import Helper

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)
    group = GroupSerializer()
    features = FeatureSerializer(many=True)

    def create(self, validated_data):        
        group_info = validated_data.pop("group")
        feature_info = validated_data.pop("features")
        
        #create a validation function for the group and feature
        
        group = Helper.get_or_create_group(group_info)
        characterisct_list = Helper.get_or_create_features(feature_info)        
        animal = Animal.objects.create(**validated_data, group=group)
        animal.features.set(characterisct_list)

        return animal

    def update(self, instance, validated_data):

        try:
            feature_info = validated_data.pop("features")
            characterisct_list = Helper.get_or_create_features(feature_info)
            
            for feature in characterisct_list:
                instance.features.add(feature)
        
        finally:
            
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            
            return instance
