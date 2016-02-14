from rest_framework import serializers

from .models import (User, Project, Tag,
                     LanguageConfig, SenderConfig)



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


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'location', 'languages')
        depth = 1

    def create(self, validated_data):
        if 'languages' in validated_data:
            languages = validated_data.pop('languages')
        else:
            languages = None
        proyect = Project.objects.create(**validated_data)
        if languages is not None:
            proyect.languages.add(*languages)
        proyect.save()
        return proyect

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')

    def create(self, validated_data):
        tag = Tag.objects.create(**validated_data)
        return tag


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
