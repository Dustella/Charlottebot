FROM python:3.10.6-alpine3.16

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apk update \
    && apk add --virtual build-dependencies build-base gcc \
    && apk add tzdata \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-dependencies

COPY . .

CMD [ "hypercorn", "bot:app", "-b", "0.0.0.0:8765" ]
