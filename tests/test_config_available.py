import boto3
import os


def test_config_available():
    session = boto3.Session()
    assert session.region_name == 'eu-central-1'  # see test_config/config


def test_env_variables_available():
    assert os.environ['AWS_ROLE_SESSION_NAME'] == 'test-role-session-name'  # see run_tests.sh


def test_credentials_available():
    session = boto3.Session()
    assert session.get_credentials() is not None
