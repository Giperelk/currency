manage := python app/manage.py


run:
	$(manage) runserver

migrate:
	$(manage) migrate

makemigrations:
	$(manage) makemigrations

shell:
	$(manage) shell_plus --print-sql
