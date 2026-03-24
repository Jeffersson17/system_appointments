lint:
	flake8 ./django/
	isort --check-only ./django/
	pylint --ignore-paths=manage.py ./django/