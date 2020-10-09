FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1

# install packages
RUN apt-get update
RUN apt-get install -y netcat ntpdate build-essential
RUN pip install virtualenv

RUN mkdir /code
WORKDIR /code

ADD . /code/

RUN python3 -m venv ~/.venvs/{{cookiecutter.repo_name}}venv && \
    . ~/.venvs/{{cookiecutter.repo_name}}venv/bin/activate && \
    pip install -r requirements.txt && \
    pip install -r dev_requirements.txt

