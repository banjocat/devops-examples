FROM ubuntu:trusty
ARG VERSION=v2.5.6
WORKDIR /opt/
ADD https://github.com/gravitational/teleport/releases/download/$VERSION/teleport-$VERSION-linux-amd64-bin.tar.gz .
RUN tar xf teleport-${VERSION}-linux-amd64-bin.tar.gz
WORKDIR /opt/teleport/
RUN mkdir -p /var/lib/teleport
RUN ./install
CMD ./teleport start
