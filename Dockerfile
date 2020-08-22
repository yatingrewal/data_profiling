# FROM tiangolo/uwsgi-nginx-flask:python3.7

FROM python:3.7-slim-buster
COPY requirements.txt /requirements.txt
RUN pip install  -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "dashboard.py" ]
