import boto3

def test_credentials_available():
    session = boto3.Session()
    assert session.get_credentials() is not None
