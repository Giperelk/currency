import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


@pytest.fixture(autouse=True, scope='function')
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture()
def authorized_api_client():
    client = APIClient()
    User = get_user_model()
    client.force_authenticate(
        user=User.objects.last()
    )
    yield client


@pytest.fixture()
def not_authorized_api_client():
    client = APIClient()
    yield client


@pytest.fixture(autouse=True, scope='session')
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'users.json',
            'sources.json',
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')
