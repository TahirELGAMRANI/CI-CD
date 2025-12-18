import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert 'CI/CD' in response.json['message']

def test_info_endpoint(client):
    """Test API info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json['language'] == 'Python'

