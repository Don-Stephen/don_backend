from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from users.views import (UserViewSet, ProjectViewSet, TagViewSet,
                         LanguageConfigViewSet, SenderConfigViewSet)
from bdd.views import (FeatureViewSet, ScenarioViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'tags', TagViewSet)
router.register(r'scenarios', ScenarioViewSet)
router.register(r'languageconfig', LanguageConfigViewSet)
router.register(r'senderconfig', SenderConfigViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include(router.urls)),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
