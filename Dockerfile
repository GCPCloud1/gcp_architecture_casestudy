FROM python:3.7-slim-buster

WORKDIR /gcp_architecture_casestudy

COPY requirements.txt requirements

ADD . .

CMD [ "python", "patient.py" ]
