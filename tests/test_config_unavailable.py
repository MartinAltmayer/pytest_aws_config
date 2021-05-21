import boto3
import os
from pathlib import Path


def test_config_unavailable():
    session = boto3.Session()
    assert session.available_profiles == []


def test_env_variables_unavailable():
    # Mocked variables
    assert os.environ['AWS_DEFAULT_REGION'] == 'us-east-1'
    assert not Path(os.environ['AWS_CONFIG_FILE']).exists()
    assert not Path(os.environ['AWS_SHARED_CREDENTIALS_FILE']).exists()

    # Other variables must not exist
    for key in os.environ:
        if key not in ('AWS_CONFIG_FILE', 'AWS_SHARED_CREDENTIALS_FILE', 'AWS_DEFAULT_REGION'):
            assert not key.startswith('AWS_')


def test_credentials_unavailable():
    session = boto3.Session()
    assert session.get_credentials() is None


def test_can_create_client():
    assert boto3.client('sqs')
