PYTHON = .venv/bin/python
DDCKER_COMPOSE = docker compose

create_env:
	cp .env_sample .env

start_db:
	$(DDCKER_COMPOSE) -f .deploy/ue-postgres-compose.yml up -d

stop_db:
	$(DDCKER_COMPOSE) -f .deploy/ue-postgres-compose.yml down -v

restart_db: stop_db start_db

migrate:
	$(PYTHON) manage.py migrate

test:
	$(PYTHON) manage.py test

start:
	$(PYTHON) manage.py runserver

run: create_env restart_db migrate start