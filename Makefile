test-flake8:
	docker-compose run --rm seba flake8 .

test-mypy:
	docker-compose run --rm seba mypy .

test-pytest:
	docker-compose run --rm seba pytest .
