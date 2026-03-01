import os

from django.contrib import admin
from django.http import JsonResponse
from django.views.generic.base import RedirectView
from django.urls import include, path

from octofit_tracker.views import router

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
if CODESPACE_NAME:
    base_url = f"https://{CODESPACE_NAME}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


def api_root(_request):
    return JsonResponse(
        {
            'users': f'{base_url}/api/users/',
            'teams': f'{base_url}/api/teams/',
            'activities': f'{base_url}/api/activities/',
            'leaderboard': f'{base_url}/api/leaderboard/',
            'workouts': f'{base_url}/api/workouts/',
        }
    )

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False), name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
