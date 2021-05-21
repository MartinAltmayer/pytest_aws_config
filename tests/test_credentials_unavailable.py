import boto3

def test_credentials_unavailable():
    session = boto3.Session()
    assert session.get_credentials() is None
