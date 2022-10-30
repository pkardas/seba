test-flake8:
	docker-compose run --rm seba flake8 .

test-mypy:
	docker-compose run --rm seba mypy .

test-pytest:
	docker-compose run --rm seba pytest .

ec2-list:
	sudo docker ps

ec2-build:
	sudo docker-compose build worker

ec2-run:
	sudo docker-compose up --detach worker

