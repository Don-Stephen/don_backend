from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import (User, Proyect, Feature, Scenario,
                     LanguageConfig, SenderConfig, Tag)

from .permissions import IsOwnerOrReadOnly
from .serializers import (CreateUserSerializer, UserSerializer, 
                          ProyectSerializer, FeatureSerializer,
                          TagSerializer, ScenarioSerializer,
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


class ProyectViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Proyects
    """
    queryset = Proyect.objects.all()
    serializer_class = ProyectSerializer
    permission_classes = (AllowAny,)


class FeatureViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Features
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (AllowAny,)


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


class ScenarioViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives Scenarioes
    """
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
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
