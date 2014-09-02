
setup:
	@pip install -qr requirements.txt

test:
	py.test

.PHONY: run
run:
	@python manage.py runserver
