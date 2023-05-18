import pytest
from ..models import User
from django.test import TestCase


class ConfTest(TestCase):
    @pytest.mark.django_db
    def test_register_success(self):
        superuser = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="admin"
        )
        superuser.save()
        assert User.objects.count() > 0

    @pytest.mark.django_db
    def create_test_user(self):
        test_user = User.objects.create(
            username="test_user",
            email="test_user@test_user.com",
            password="test_user"
        )
        test_user.save()
        return test_user

