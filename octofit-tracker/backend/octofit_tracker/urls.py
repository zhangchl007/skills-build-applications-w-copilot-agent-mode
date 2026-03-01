import os

from django.contrib import admin
from django.urls import include, path

from octofit_tracker.views import api_root, router

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('', api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
