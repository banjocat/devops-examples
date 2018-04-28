FROM python:3

RUN pip install --upgrade pip

RUN pip install apache-airflow

RUN airflow initdb

CMD airflow webserver -p 8080
