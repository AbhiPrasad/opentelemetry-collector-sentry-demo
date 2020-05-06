docker_compose:
	docker-compose build
	docker-compose run -d -p 3003:3003 flask
.PHONY: docker_compose

down:
	docker-compose down
.PHONY: down
