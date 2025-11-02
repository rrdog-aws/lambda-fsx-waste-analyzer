import pytest
import requests
import os
import json

API_ENDPOINT = os.getenv('TEST_API_ENDPOINT')

def test_api_endpoint():
    # Make request to the API
    response = requests.get(API_ENDPOINT)
    
    # Assert status code is 200
    assert response.status_code == 200
    
    # Parse response
    data = response.json()
    
    # Check response structure
    assert 'timestamp' in data
    assert 'results' in data
    
    # Check that results is a list
    assert isinstance(data['results'], list)
    
    # Check that each result has required fields
    for result in data['results']:
        assert 'fsid' in result
        assert 'state' in result
        assert 'storage_gib' in result

def test_api_headers():
    response = requests.get(API_ENDPOINT)
    
    # Check CORS headers
    assert response.headers['Access-Control-Allow-Origin'] == '*'
    assert response.headers['Content-Type'] == 'application/json'
