build:
	DOCKER_BUILDKIT=1 docker build --platform linux/amd64 --build-arg arch=linux/amd64 -t ${CONTAINER_NAME} .

run:
	docker run --platform linux/amd64 -p 8080:8080 -v ~/.aws:/root/.aws ${CONTAINER_NAME}:latest

push:
	docker tag ${CONTAINER_NAME}:latest ${ECR_REPOSITORY_URI}
	aws ecr get-login-password | docker login --username AWS --password-stdin ${ECR_REPOSITORY_URI}
	docker push ${ECR_REPOSITORY_URI}

test_unit:
	pytest tests/test_unit.py

test_api_gateway:
	API_URL=${API_URL} pytest tests/test_api_gateway.py
