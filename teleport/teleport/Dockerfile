FROM ubuntu:trusty
ARG VERSION=v2.5.4
WORKDIR /opt/
ADD https://github.com/gravitational/teleport/releases/download/$VERSION/teleport-$VERSION-linux-amd64-bin.tar.gz .
RUN tar xf teleport-v2.5.4-linux-amd64-bin.tar.gz
WORKDIR /opt/teleport/
RUN mkdir -p /var/lib/teleport
CMD ./teleport start
