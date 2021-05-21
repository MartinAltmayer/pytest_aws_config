#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"

docker build . -t pytest_aws_config

docker run --rm \
  --env AWS_ROLE_SESSION_NAME="test-role-session-name" \
  pytest_aws_config \
  -p no:pytest_aws_config \
  /opt/tests/test_config_available.py

docker run --rm \
  --env AWS_ROLE_SESSION_NAME="test-role-session-name" \
  pytest_aws_config \
  /opt/tests/test_config_unavailable.py
