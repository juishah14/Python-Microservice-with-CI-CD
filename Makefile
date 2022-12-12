install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
	python -m textblob.download_corpora

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
	docker build -t deploy-fastapi .
run:
	#run docker on http://localhost:8080/
	#docker run -p 8080:8080 fe04d251e3be
deploy:
	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest

all: install post-install lint test deploy