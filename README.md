# Gunicorn serve deployment

## Local run:

### Development host
1. Prerequisites
* python version equal to pyproject.toml python
* poetry
2. Install dependencies
```bash
poetry install
```
3. Run server
```bash
gunicorn src.main:app --config src/configs/gunicorn_config.py --log-config src/configs/logging_gunicorn_config.conf --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80  --workers 1
```
4. Go to http://localhost/docs

### Development docker
1. Build docker
```bash
docker build -t server .
```
2. Run server in docker
```bash
docker run -p 80:80 server
```
3. Go to http://localhost/docs

### Docker compose
1. login to AWS SSO
```bash
aws sso login --profile {your_aws_profile:dwh-stage}
```
2. run the following code in terminal:
```bash
docker compose -f docker-compose.yaml up
```
3. Go to http://localhost/docs
