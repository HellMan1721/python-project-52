install:
	uv sync --dev

dev-start:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

check:
	uv run ruff check

test:
	uv run manage.py test

test-coverage:
	uv run coverage erase
	uv run coverage run --source=task_manager,tasks manage.py test
	uv run coverage xml -i
	uv run coverage report -m

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

push:
	git add . & git commit -m 'thangs' & git push