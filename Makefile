install:
	uv sync --dev

dev-start:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

lint:
	ruff check

test:
	uv run manage.py test

test-coverage:
	coverage run manage.py test

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

push:
	git add . & git commit -m 'thangs' & git push