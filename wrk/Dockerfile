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

ENV CONNECTIONS 300
ENV THREADS 3
ENV URL localhost
ENV DURATION 10

COPY ./script.lua /tmp/.
CMD ./wrk -s /tmp/script.lua -d $DURATION -t $THREADS -c $CONNECTIONS http://${URL}
