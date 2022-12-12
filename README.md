[![Deploy to Amazon ECS](https://github.com/juishah14/Python-Microservice-with-CI-CD/actions/workflows/devops.yml/badge.svg)](https://github.com/juishah14/Python-Microservice-with-CI-CD/actions/workflows/devops.yml)

# Python Microservice with CI/CD

### Tools: Fast API, Nasa API, Docker, Aws ECR, Aws Codebuild, Aws App Runner

This is a Python Microservice equipped with CI/CD, that can be scaled and used to create a production-level Dev-Ops workflow and infrastructure.

<br>

Continuous Integration: <br>
A Github workflow has been set up to aid in facilitating smooth continuous integration. The workflow performs a build which installs dependencies, formats and lints code, runs tests, and containerizes code, as well as sends an email to the repo owner upon any build failures.

<br>

Continuous Deployment: <br>
In order to set up containerized continuous deployment, this repo can be connected to AWS Codebuild. This will allow for new images to be built upon any pushes to main, and for these images to then be pushed directly to ECR. <br>

To set this up, create a build project with AWS Codebuild and configure it such that:

1. It allows for webhooks (so that a new image for the container will be built upon any changes to main)
2. It uses a buildspec.yml file which uses the commands listed in the Makefile (eg. make format, make deploy, etc.)

After this, ECR can be connected to either AWS ECS or AWS App Runner, in order to continuously deploy our newest container.

To use ECS, create a cluster and then a new service which uses that cluster. The service should be given a task definition so that it knows which Docker image to use from ECR.

To use App Runner, create a service which uses ECR. App Runner can then monitor your container registry and deploy a new version of your service for each image push. It will also give you a domain/url on which your service (in this case an API) is being hosted.

<br>

Local Development: <br>
Enter virtual environment - `venv/Scripts/Activate.ps1` <br>
Build, test, and run locally -

1. `docker build -t nasa-api .`
2. `docker images`
3. `docker run -p 8080:8080 <image-id>`

<br>

Note: (Insert description later of how to use this api and that there are routes etc. and an image of the worflow ie. CD of Containerized Paas Microservice, similar process to what you'd do to build out NLP Microservices on AWS)
