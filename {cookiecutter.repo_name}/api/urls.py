from django.conf.urls import url

from {{cookiecutter.repo_name}}.api.views.heartbeat import heartbeat


urlpatterns = [
    url(r'^heartbeat/$', heartbeat, name='heartbeat'),
]
