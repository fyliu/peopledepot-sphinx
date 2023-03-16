import pytest
from django.db.models.deletion import RestrictedError

pytestmark = pytest.mark.django_db


def test_user(user, django_user_model):
    assert django_user_model.objects.filter(is_staff=False).count() == 1
    assert str(user) == "testuser@email.com"
    assert user.is_django_user is True
    assert repr(user) == f"<User {user.uuid}>"


def test_project(project):
    assert str(project) == "Test Project"


def test_recurring_event(recurring_event):
    assert str(recurring_event) == "Test Recurring Event"


def test_sponsor_partner(sponsor_partner):
    assert str(sponsor_partner) == "Test Sponsor Partner"


def test_faq(faq):
    assert str(faq) == "Test Faq"


def test_faq_viewed(faq_viewed):
    assert str(faq_viewed).startswith("Test Faq viewed")


def test_location(location):
    assert str(location) == "Test Hack for L.A. HQ"


def test_create_user_status(user):
    from ..models import UserStatus

    payload = {
        "name": "test user status",
    }
    user_status = UserStatus(**payload)

    assert str(user_status) == payload["name"]


def test_assign_user_status_to_user(user, user_status):
    user_status.save()

    assert user_status.users.count() == 0

    user.status = user_status
    user.save()

    assert str(user.status) == user_status.name
    assert user_status.users.count() == 1


def test_delete_user_status(user, user_status):
    user_status.save()

    user.status = user_status
    user.save()

    # delete is protected and raises an exception
    with pytest.raises(RestrictedError):
        user_status.delete()
