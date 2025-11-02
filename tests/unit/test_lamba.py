import json
import pytest
from src.lambda_function import lambda_handler

def test_lambda_handler():
    # Test event
    event = {}
    context = {}
    
    # Call the handler
    response = lambda_handler(event, context)
    
    # Assert response format
    assert isinstance(response, dict)
    assert 'statusCode' in response
    assert 'body' in response
    assert 'headers' in response
    
    # Assert status code is 200
    assert response['statusCode'] == 200
    
    # Parse body and check structure
    body = json.loads(response['body'])
    assert 'timestamp' in body
    assert 'results' in body

def test_response_headers():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    
    # Check CORS headers
    assert response['headers']['Access-Control-Allow-Origin'] == '*'
    assert response['headers']['Content-Type'] == 'application/json'
