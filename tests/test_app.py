import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Test Event",
        "description": "Test Description",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00"
    })
    assert response.status_code == 201

def test_list_events(client):
    response = client.get('/events')
    assert response.status_code == 200
