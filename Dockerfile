FROM python:3.8.17-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache make

RUN make setup

RUN make init-db

RUN make populate-db

EXPOSE 5000

CMD [ "make", "run" ]