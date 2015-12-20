from rest_framework import serializers

from .models import (User, Proyect, Feature, Scenario,
                     LanguageConfig, SenderConfig, Tag)
                     


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        write_only_fields = ('password',)


class ProyectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyect
        fields = ('id', 'name', 'location', 'languages')

    def create(self, validated_data):
        if 'languages' in validated_data:
            languages = validated_data.pop('languages')
        else:
            languages = None
        proyect = Proyect.objects.create(**validated_data)
        if languages is not None:
            proyect.languages.add(*languages)
        proyect.save()
        return proyect


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id', 'language', 'description', 'finality', 'who', 'purpose', 'proyect')

    def create(self, validated_data):
        feature = Feature.objects.create(**validated_data)
        return feature


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag


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


class LanguageConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageConfig

    def create(self, validated_data):
        languageconfig = LanguageConfig.objects.create(**validated_data)
        return languageconfig


class SenderConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = SenderConfig

    def create(self, validated_data):
        senderconfig = SenderConfig.objects.create(**validated_data)
        return senderconfig 
