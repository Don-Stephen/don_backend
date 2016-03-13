from rest_framework import serializers

from .models import Feature, Scenario, Tag


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id', 'language', 'description', 'finality', 'who', 'purpose', 'project')

    def create(self, validated_data):
        feature = Feature.objects.create(**validated_data)
        return feature

class ScenarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scenario
        depth = 2

    def create(self, validated_data):
        if 'tags' in validated_data:
            tags = validated_data.pop('tags')
        else:
            tags = None
        scenario = Scenario.objects.create(**validated_data)
        if tags is not None:
            scenario.tags.add(*tags)
        return scenario


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag
