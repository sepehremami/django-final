
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_view(client):
    url = reverse('product')
    response = client.get(url)
    assert response.status_code == 200
