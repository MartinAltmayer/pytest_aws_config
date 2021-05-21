import os
from uuid import uuid4


def pytest_configure(config):
    non_existing_file = f"/tmp/{uuid4()}"
    os.environ["AWS_CONFIG_FILE"] = non_existing_file
    os.environ["AWS_SHARED_CREDENTIALS_FILE"] = non_existing_file
