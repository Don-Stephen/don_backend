from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import (User, Project, Tag,
                     LanguageConfig, SenderConfig)

from .permissions import IsOwnerOrReadOnly
from .serializers import (CreateUserSerializer, UserSerializer,
                          ProjectSerializer, TagSerializer,
                          LanguageConfigSerializer, SenderConfigSerializer)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class ProjectViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Projects
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        project = self.serializer_class(data=request.data)
        if project.is_valid():
            project = project.create(validated_data=project.data)
            if 'languages' in request.data:
                project.languages.add(*LanguageConfig.objects.filter(id__in=request.data['languages']))
            return Response(data=self.serializer_class(project).data, status=201)
        else:
            return Response(data=project.errors, status=400)

class TagViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class LanguageConfigViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Scenarioes
    """
    queryset = LanguageConfig.objects.all()
    serializer_class = LanguageConfigSerializer
    permission_classes = (AllowAny,)


class SenderConfigViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Scenarioes
    """
    queryset = SenderConfig.objects.all()
    serializer_class = SenderConfigSerializer
    permission_classes = (AllowAny,)
