manage := python app/manage.py


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

flake8:
	flake8 app

worker:
	cd app && celery -A settings worker -l info --autoscale=0,10

beat:
	cd app && celery -A settings worker -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html
