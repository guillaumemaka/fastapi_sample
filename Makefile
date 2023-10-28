# Targets:
# - starttestdb: creates and starts a Docker container for the test database, and sets the DATABASE_URL environment variable
# - stoptestdb: stops and removes the Docker container for the test database
# - activateenv: activates the virtual environment for the project
# - migratedb: upgrades the test database to the latest migration using Alembic
# - testwatch: runs the tests continuously using pytest-watch
# - tests: runs the tests once using pytest and stops the test database container

# set default tartget
.DEFAULT_GOAL := tests

.PHONY: starttestdb startdb createvenv startserver stoptestdb activateenv migratedb testwatch tests

export DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5267/postgres_test

starttestdb:
	@docker compose create testdb
	@docker compose start testdb

startdb:
	@docker compose create db
	@docker compose start db

stoptestdb:
	@docker compose stop testdb
	@docker compose rm testdb -f

createvenv:
	if [ ! -d "venv" ]; then \
		@pip install virtualenv; \
		@echo "Creating virtual environment"; \
		@python -m virtualenv venv; \
	fi

activateenv: createvenv
	@echo "Activating virtual environment"
	@. venv/bin/activate

migratedb: starttestdb activateenv
	@echo "Upgrading test database to latest migration"
	@poetry run alembic upgrade head

testwatch: migratedb
	@poetry run ptw

tests: migratedb
	@poetry run pytest -vvv
	@make stoptestdb

startserver: startdb activateenv
	@export DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5342/postgres
	@make migratedb
	@poetry run uvicorn main:app --reload

startindocker:
	@docker compose up --build