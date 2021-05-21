ARG  PYTHON_VERSION=latest
FROM python:${PYTHON_VERSION}-alpine3.13

RUN pip install pytest boto3

ENV AWS_ROLE_SESSION_NAME=test-role-session-name

COPY test_config/ /root/.aws
COPY tests/ /opt/tests
COPY pytest_aws_config.py setup.cfg pyproject.toml /opt/pytest_aws_config/

RUN pip install --use-feature=in-tree-build /opt/pytest_aws_config

ENTRYPOINT ["sh", "/opt/tests/run_in_docker.sh"]
