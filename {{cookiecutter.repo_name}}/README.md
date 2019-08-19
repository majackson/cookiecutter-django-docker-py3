# {{cookiecutter.project_name}} 

## Overview

The {{cookiecutter.project_name}} project is a python3/django/postgres/docker project.

This project is originally cut from a cookiecutter located at https://github.com/majackson/cookiecutter-django-docker-py3/.

## Developer Setup

The project is fully dockerised. There are a few ways to set this up on a Mac, but I'd recommend using `docker-machine`. You'll also need homebrew, VirtualBox, docker and docker-compose.

Once Docker and docker-compose (and make) are installed and configured, the project can be set up with `make bootstrap`.

## Tests

Run tests with `make test`.

## Development Server

To run a development server, use `make run`. The server will be up on your docker VM (get this with `docker-machine ip default` if you are using docker-machine), port 80.

## Changing Development Environment

If any of the libraries in `requirements.txt` or `dev_requirements.txt` are changed, `make dev-build` will have to be rerun before they are reflected in runs of `make test` or `make run`.
