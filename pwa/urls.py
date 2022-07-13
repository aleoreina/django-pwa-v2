from django.urls import include, path

from .views import manifest, service_worker, offline
from . import app_settings


# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    path('serviceworker.js', service_worker, name='serviceworker'),
    path('manifest.json', manifest, name='manifest'),
]


if app_settings.PWA_CUSTOM_OFFLINE_PAGE == False:
    urlpatterns += path('offline', offline, name='offline')
