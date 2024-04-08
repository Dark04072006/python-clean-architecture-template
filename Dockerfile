FROM python:3.11.5-alpine

WORKDIR /source/

COPY conf/ /source/conf/
COPY src/ /source/src/

COPY pyproject.toml /source/pyproject.toml

RUN pip install -U pip
RUN pip install -e .
