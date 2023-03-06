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
