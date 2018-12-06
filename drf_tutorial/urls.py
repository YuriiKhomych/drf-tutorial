from django.conf.urls import url, include
from django.urls import path

from rest_framework import routers
from rest_framework.schemas import get_schema_view

from quickstart.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('', include('snippets.urls')),
    path('schema/', schema_view),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
