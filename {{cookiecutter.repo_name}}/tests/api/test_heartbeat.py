import pytest

from django.urls import reverse

from django.test import Client

from rest_framework import status


def test_heartbeat_ok():
    resp = Client().get(reverse('heartbeat-ok'))
    assert resp.status_code == status.HTTP_200_OK


def test_heartbeat_error():
    with pytest.raises(Exception):
        Client().get(reverse('heartbeat-error'))
