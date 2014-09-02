
setup:
	@pip install -qr requirements.txt

test:
	MONGODB_URL=twitter_watcher_test py.test

.PHONY: run
run:
	@python manage.py runserver
