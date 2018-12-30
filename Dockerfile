FROM python:3.6-alpine

RUN apk update && apk add libpq

RUN apk add --virtual .build-dependencies \
            --no-cache \
            gcc \
            python3-dev \
            build-base \
            linux-headers \
            musl-dev \
            postgresql-dev \
            pcre-dev

RUN apk add --no-cache pcre

WORKDIR /home/unbabel

COPY ./app /home/unbabel/app
COPY ./settings.py /home/unbabel
COPY ./requirements.txt /home/unbabel
COPY ./config /home/unbabel/config

RUN pip install --no-cache-dir -r /home/unbabel/requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*