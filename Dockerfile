FROM python:3.10-alpine3.15

WORKDIR /src

COPY requirements.txt src/requirements.txt
RUN pip install -r src/requirements.txt

COPY . /src

