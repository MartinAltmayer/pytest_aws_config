import os
from uuid import uuid4
from tempfile import gettempdir


def pytest_configure(config):
    # Docs on AWS environment variables:
    # https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html
    aws_environment_variables = [key for key in os.environ if key.startswith('AWS_')]
    for key in aws_environment_variables:
        del os.environ[key]

    non_existing_folder = os.path.join(gettempdir(), str(uuid4()))
    os.environ['AWS_CONFIG_FILE'] = os.path.join(non_existing_folder, 'config')
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = os.path.join(non_existing_folder, 'credentials')

    # We must specify some region or e.g. boto3.client('sqs') fails
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
