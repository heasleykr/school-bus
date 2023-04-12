# Docker-compose
build: ## Build all docker images.
	docker-compose build --pull --parallel
up: ## Run all services
	docker-compose up
up-build: ## Build and run all services
	docker compose up --build
clean: ## Clean up docker containers.
	docker-compose kill
	docker-compose rm --force

# Django Schoolbus Project
manage: ## Run a Django management command. Usage: make C=<command> manage
	docker-compose run schoolbus bash -c "./ manage.py $(C)"
makemigrations: ## Make DB migrations.
	docker compose run schoolbus bash -c "./manage.py makemigrations"
migrate: ## Run DB migrations.
	docker compose run schoolbus bash -c "./manage.py migrate"
run: ## Run the schoolbs development server.
	docker-compose up schoolbus
shell: ## Drop into a python shell. 'exit' to exit.
	docker compose run schoolbus bash
