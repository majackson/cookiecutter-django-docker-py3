from django.conf.urls import url

from {{cookiecutter.repo_name}}.api.views.heartbeat import heartbeat_ok, heartbeat_error


urlpatterns = [
    url(r'^heartbeat/ok/$', heartbeat_ok, name='heartbeat-ok'),
    url(r'^heartbeat/error/$', heartbeat_error, name='heartbeat-error'),
]
