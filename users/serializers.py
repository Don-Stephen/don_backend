from rest_framework import serializers

from .models import (User, Project,
                     LanguageConfig, SenderConfig)

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
        fields = ('id', 'name', 'languages')
        depth = 1

    def create(self, validated_data):

        project = Project.objects.create(**validated_data)
        project.save()
        return project

