FROM python:3.7-slim-buster

WORKDIR /app
ADD . /app

COPY requirements.txt requirements

ENV PORT 8080

CMD [ "python", "patient.py" ]
