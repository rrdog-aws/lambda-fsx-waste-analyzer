import pytest
import requests
import os
import json

def test_api_endpoint():
    api_endpoint = os.getenv('TEST_API_ENDPOINT')
    assert api_endpoint is not None, "TEST_API_ENDPOINT environment variable is not set"
    
    # Make request to the API
    response = requests.get(api_endpoint)
    
    # Assert status code is 200
    assert response.status_code == 200
    
    # Verify response is JSON
    response_data = response.json()
    assert isinstance(response_data, dict)

def test_api_headers():
    api_endpoint = os.getenv('TEST_API_ENDPOINT')
    response = requests.get(api_endpoint)
    
    # Check headers
    assert 'Access-Control-Allow-Origin' in response.headers
    assert 'Content-Type' in response.headers
