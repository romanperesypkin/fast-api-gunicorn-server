FROM python:3.10-slim-buster

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

ARG ENV=stage
ARG VERSION=0.0.1
ARG PROMETHEUS_MULTIPROC_DIR=/tmp
ARG SOURCE_VENV_DIR=/usr/local/venv/bin/activate
ARG GUNICORN_CMD_ARGS
ARG DEV_BUILD=--no-dev

RUN apt-get update -q &&  \
    apt-get install --no-install-recommends --yes curl &&  \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local POETRY_VERSION=1.4.2 python3 -

COPY pyproject.toml .
COPY poetry.lock .

RUN source $SOURCE_VENV_DIR && \
    pip install --no-cache-dir urllib3==1.26.15 && \
    deactivate && \
    poetry config http-basic.gitlab $PYPI_USERNAME $PYPI_PASSWORD && \
    poetry config virtualenvs.create false && \
    poetry install $DEV_BUILD && \
    rm -rf ~/.cache/{pip,pypoetry}

COPY src src

ENV APP_VERSION=$VERSION
ENV PROMETHEUS_MULTIPROC_DIR=$PROMETHEUS_MULTIPROC_DIR
ENV GUNICORN_CMD_ARGS=$GUNICORN_CMD_ARGS
ENV ENV=$ENV

CMD ["gunicorn", "src.main:app", \
    "--config", "src/configs/gunicorn_config.py", \
    "--log-config", "src/configs/logging_gunicorn_config.conf", \
    "--worker-class", "uvicorn.workers.UvicornWorker", \
    "--bind", "0.0.0.0:80", \
    "--workers", "1"]
