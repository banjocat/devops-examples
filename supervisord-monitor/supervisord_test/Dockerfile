FROM python:2

RUN pip install supervisor
RUN mkdir -p /var/log/supervisord

COPY ./supervisord.conf /etc/supervisord.conf
RUN mkdir -p /www
COPY ./index.html /www/index.html

EXPOSE 9001
CMD supervisord -c /etc/supervisord.conf

