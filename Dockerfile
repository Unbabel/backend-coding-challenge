FROM python:3-alpine

RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            postgresql-dev \
            pcre-dev

RUN apk add --no-cache pcre

RUN /home/unbabel/app

COPY ./app /home/unbabel/app
COPY ./run.py /home/unbabel/app/
COPY ./settings.py /home/unbabel/app/
COPY ./requirements.txt /home/unbabel/app
COPY ./requirements-prod.txt /home/unbabel/app

RUN pip install --no-cache-dir -r /home/unbabel/app/requirements.txt
RUN pip install --no-cache-dir -r /home/unbabel/app/requirements-prod.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

COPY /config /home/unbabel/config