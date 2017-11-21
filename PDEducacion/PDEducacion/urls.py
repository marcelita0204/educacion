from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from  appSeguridad.views import (
    AplicacionViewSet,
    PermisoViewSet,
    RolViewSet
)

router = routers.DefaultRouter()
router.register(r'aplicaciones',AplicacionViewSet)
router.register(r'permisos',PermisoViewSet)
router.register(r'roles',RolViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(
        r'^appUniversidad/',
        include('appUniversidad.urls')
    ),
]
