FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
        wget \
        ca-certificates \
        apt-transport-https
RUN wget -O- https://sensu.global.ssl.fastly.net/apt/pubkey.gpg | apt-key add -
RUN echo "deb https://sensu.global.ssl.fastly.net/apt sensu main" > /etc/apt/sources.list.d/sensu.list
RUN apt-get update && apt-get install -y sensu
ENV PATH="/opt/sensu/bin:${PATH}"

