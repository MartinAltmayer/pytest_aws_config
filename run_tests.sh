#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")"

# We use docker instead of tox so that we can overwrite ~/.aws/{config,credentials}

if [[ "$#" -eq 0 ]]; then
  python_versions="3.6.13 3.7.10 3.8.10 3.9.5"
else
  python_versions="$@"
fi

for version in $python_versions; do
  echo "Testing with Python $version..."
  tag="pytest-aws-config:$version"
  docker build . -t "$tag" --build-arg "PYTHON_VERSION=$version"
  docker run --rm "$tag"
done
