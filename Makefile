install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py library/*.py
lint:
	#check proper syntax via flake8 or pylint
	pylint --disable=R,C *.py library/*.py
test:
	#test
	python -m pytest -vv --cov=library --cov=main test_*.py
build:
	#build container
	docker build -t nasa-api .
deploy:
	#deploy
	aws ecr get-login-password --region canada-central | docker login --username AWS --password-stdin <id>.dkr.ecr.canada-central.amazonaws.com
	docker build -t nasa-api .
	docker tag nasa-api:latest <id>.dkr.ecr.canada-central.amazonaws.com/nasa-api:latest
	docker push <id>.dkr.ecr.canada-central.amazonaws.com/nasa-api:latest