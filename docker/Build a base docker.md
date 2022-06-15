如果只有一個Dockerfile(如下)
每次更版都會跑到"pip install -r requirements.txt"
但其實每次的套件都沒變, 每次跑等於浪費時間與網路

```
# Dockerfile
FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings
RUN mkdir /mydjangoproject
WORKDIR /mydjangoproject
COPY . .
RUN pip install -r requirements.txt
```

可以寫一個base的Docker image, 然後再讓專案的去用base的image
這樣只要花費COPY的時間即可更版

```
# DockerfileBase
# Build base的image : docker build . -f DockerfileBase -t mybase
FROM python:3.7

RUN mkdir /requirements

WORKDIR /requirements

COPY requirements.txt /requirements/requirements.txt

RUN pip install -r /requirements/requirements.txt
```

```
# Dockerfile
FROM mybase

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings

RUN mkdir /mydjangoproject

WORKDIR /mydjangoproject

COPY . .
```