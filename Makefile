
.PHONY: setup
setup:
	@pip install -r requirements.txt

.PHONY: test
test:
	@MONGODB_URL=twitter_watcher_test py.test

.PHONY: run
run:
	@python manage.py runserver
