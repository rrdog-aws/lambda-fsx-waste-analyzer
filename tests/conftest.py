import os
import sys
import pytest

# Get the absolute path of the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, 'src')

# Add the src directory to the Python path
sys.path.insert(0, src_path)

@pytest.fixture
def lambda_event():
    return {}

@pytest.fixture
def lambda_context():
    return {}
