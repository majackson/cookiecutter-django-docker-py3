dev-build:
	docker-compose run --name {{cookiecutter.repo_name}}_api_cleanup --rm api bash -c "rm -rf ~/.venvs/{{cookiecutter.repo_name}}venv" && \
	docker-compose build

update-time:
	docker-machine ssh default "sudo ntpclient -s -h pool.ntp.org"

django:
	docker-compose run --service-ports --name {{cookiecutter.repo_name}}_api_django --rm api bash -c "source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && python manage.py ${DJANGO_CMD}"

staticfiles:
	DJANGO_CMD="collectstatic --no-input" make django

shell:
	DJANGO_CMD=shell make django

migrate:
	DJANGO_CMD=migrate make django	

zappa:
	make update-time && \
	docker-compose run --name {{cookiecutter.repo_name}}_api_zappa --rm api bash -c "source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && zappa ${ZAPPA_CMD}"

bootstrap:
	cp -n production.env.template production.env && \
	make dev-build staticfiles wait-for-db migrate

run:
	echo "Server will be coming up at http://`docker-machine ip`/" && \
	ADMIN=TRUE DEBUG=TRUE docker-compose up

serve:
	docker-compose start

serve-restart:
	docker-compose restart

serve-stop:
	docker-compose stop

test:
	docker-compose run --name {{cookiecutter.repo_name}}_api_tests --rm api bash -c 'source ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && py.test --strict $${TEST_ARGS:-"tests/"}'

wait-for-db:  # hack just to block until the database is available
	docker-compose run --name {{cookiecutter.repo_name}}_api_django --rm api bash -c "while ! nc -w 1 -z db 5432; do sleep 0.1; done;"
