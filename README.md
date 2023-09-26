# REDIS-FASTAPI Boilerplate Code with Docker

This project is a boilerplate for building a Python API with Redis and FastAPI. It
includes a Docker configuration for running the API and Redis in containers.

## Requirements

This project works by default on Python 3.11. You will also need to change the 
dockefile to use the version your project requires.

## Setup

This project is designed to run as a set of Docker containers. You will need to
[install Docker](https://www.docker.com/) to complete the setup tasks.

First, clone this repo and build the Docker images for the project:

    $ git clone <>
    $ cd <ProjectName>
    $ docker-compose build

Running the API involves starting the app server and Redis. You'll do those steps
next!


## Running the API

The `docker-compose.yaml` file in this project configures containers for a Redis
instance with the RedisTimeSeries module, the Python app for the example API,
and a test runner.

Use this command to run all three containers:

    $ docker-compose up

This command starts Redis and the API server and runs the tests.

### Running Tests (TODO)

You can run the app's test suite using docker-compose:

    $ docker-compose up test
