"""
This contains configurations for our test fixtures used across test modules
"""
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticate

        # client.force_authenticate(user={}) # normal user
        # api_client.force_authenticate(user=User(is_staff=True))