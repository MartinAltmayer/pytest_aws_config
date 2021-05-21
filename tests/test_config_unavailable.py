import boto3
import os
from pathlib import Path


def test_config_unavailable():
    session = boto3.Session()
    assert not session.region_name


def test_env_variables_unavailable():
    for key in os.environ:
        if key not in ('AWS_CONFIG_FILE', 'AWS_SHARED_CREDENTIALS_FILE'):
            assert not key.startswith('AWS_')

    assert not Path(os.environ['AWS_CONFIG_FILE']).exists()
    assert not Path(os.environ['AWS_SHARED_CREDENTIALS_FILE']).exists()


def test_credentials_unavailable():
    session = boto3.Session()
    assert session.get_credentials() is None
