import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from octofit_tracker.views import router

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


def api_root(_request):
    return JsonResponse(
        {
            'teams': f'{base_url}/api/teams/',
            'profiles': f'{base_url}/api/profiles/',
            'activities': f'{base_url}/api/activities/',
            'leaderboard': f'{base_url}/api/leaderboard/',
            'workouts': f'{base_url}/api/workouts/',
        }
    )

urlpatterns = [
    path('', api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
