FROM ubuntu:trusty
RUN apt-get update && apt-get install -y \
        git \
        php5 \
        python-dev \
        python-setuptools


RUN easy_install j2cli
RUN mkdir /app
WORKDIR /app
RUN git clone https://github.com/mlazarov/supervisord-monitor.git


WORKDIR /app/supervisord-monitor
COPY ./supervisord.php.j2 .
COPY ./start_monitor.sh .
EXPOSE 80
CMD ./start_monitor.sh


