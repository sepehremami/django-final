from apps.core.models import User
import pytest
import logging


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(level=logging.INFO)


@pytest.fixture
def normal_user(db) -> User:
    return User.objects.create_user("A")  # type:ignore


@pytest.mark.django_db
def test_create_user() -> None:
    user = User.objects.create_user("User")  # type: ignore
    assert user.username == "User"


@pytest.mark.django_db
def test_user_can_see_posts(normal_user):
    logging.info(f"{normal_user}")
    assert True
