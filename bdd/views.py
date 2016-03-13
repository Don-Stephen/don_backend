from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Feature, Scenario, Tag

from .serializers import FeatureSerializer, ScenarioSerializer, TagSerializer


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
