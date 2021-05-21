#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"

docker build . -t pytest_aws_config

docker run --rm pytest_aws_config -p no:pytest_aws_config /opt/tests/test_credentials_available.py
docker run --rm pytest_aws_config /opt/tests/test_credentials_unavailable.py
