#!/usr/bin/sh
set -eu

pytest -p no:pytest_aws_config /opt/tests/test_config_available.py
pytest /opt/tests/test_config_unavailable.py
