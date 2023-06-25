#! /bin/bash

# shellcheck disable=SC1091
source .env

echo --build-arg PYPI_USERNAME="$PYPI_USERNAME"
echo --build-arg PYPI_PASSWORD="$PYPI_PASSWORD"

echo --build-arg APP_VERSION="$APP_VERSION"
echo --build-arg PROMETHEUS_MULTIPROC_DIR="$PROMETHEUS_MULTIPROC_DIR"
echo --build-arg GUNICORN_CMD_ARGS="$GUNICORN_CMD_ARGS"
echo --build-arg DEV_BUILD="$DEV_BUILD"

echo --build-arg HTTP_CONNECTION_LIMIT="$HTTP_CONNECTION_LIMIT"
echo --build-arg HTTP_REQUEST_TIMEOUT="$HTTP_REQUEST_TIMEOUT"
