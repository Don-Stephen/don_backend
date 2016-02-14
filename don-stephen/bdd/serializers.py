from rest_framework import serializers

from .models import Feature, Scenario


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id', 'language', 'description', 'finality', 'who', 'purpose', 'proyect')

    def create(self, validated_data):
        feature = Feature.objects.create(**validated_data)
        return feature

class ScenarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario

    def create(self, validated_data):
        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
        else:
            tags = None
        scenario = Scenario.objects.create(**validated_data)
        if tags is not None:
            scenario.tags.add(*tags)
        return scenario
