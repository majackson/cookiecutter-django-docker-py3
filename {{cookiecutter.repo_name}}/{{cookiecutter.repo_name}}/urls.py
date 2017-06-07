from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin


if settings.ADMIN:
    urlpatterns = [url(r'^dashboard/', admin.site.urls)]
    admin.site.site_header = "{{cookiecutter.project_name}} Administration"
else:
    urlpatterns = []

urlpatterns += [
    url(r'^', include('{{cookiecutter.repo_name}}.api.urls')),
]
