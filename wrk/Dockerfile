FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
        build-essential \
        make \
        git \
        libssl-dev

WORKDIR /tmp
RUN git clone https://github.com/wg/wrk.git
WORKDIR /tmp/wrk
RUN make -s

ENV WRK_CONNECTIONS 300
ENV WRK_THREADS 3
ENV WRK_URL localhost
ENV WRK_DURATION 10
ENV WRK_METHOD GET

COPY ./start_wrk.sh /tmp/wrk/start_wrk.sh
CMD ./start_wrk.sh
