from django.urls import path

from django_project.integrity_tests.views import CacheIntegrityView

app_name = 'integrity_tests'

urlpatterns = (
    path(f'{app_name}/test/cache', CacheIntegrityView.as_view(), name='cache-integrity-view'),
)
