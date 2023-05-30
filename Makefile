manage := docker-compose exec -it backend python manage.py


run:
	$(manage) runserver

migrate:
	$(manage) migrate

makemigrations:
	$(manage) makemigrations

createsuperuser:
	$(manage) createsuperuser

shell:
	$(manage) shell_plus --print-sql

collectstatic:
	$(manage) collectstatic --no-input && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

flake8:
	flake8 app

worker:
	cd app && celery -A settings worker -l info -c 4 --pool threads

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker-compose exec -it pytest ./app/tests --cov=app --cov-report html

docker_compose:
	docker-compose up -d --build

docker_restart:
	docker-compose down && docker-compose up -d --build && docker-compose ps -a

run_gunicorn:
	gunicorn --workers 4 settings.wsgi --max-requests 10000 --log-level info --bind 0.0.0.0:8000
