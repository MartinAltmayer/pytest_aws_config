FROM python:3.9.5-alpine3.13

RUN pip install pytest boto3

COPY test_config/ /root/.aws
COPY tests/ /opt/tests
COPY pytest_aws_config.py setup.cfg pyproject.toml /opt/pytest_aws_config/

RUN pip install --use-feature=in-tree-build /opt/pytest_aws_config

ENTRYPOINT ["pytest"]
CMD [ "/opt/tests/test_credentials_available.py" ]
