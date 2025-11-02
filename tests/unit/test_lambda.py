import json
import pytest
import os
import sys
from src.lambda_function import lambda_handler  # Update the import path

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

def test_response_headers():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    
    # Check headers
    assert 'headers' in response
    assert 'Access-Control-Allow-Origin' in response['headers']
    assert 'Content-Type' in response['headers']
