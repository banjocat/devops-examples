FROM nginx:stable

RUN apt-get update -y && apt-get install -y \
        python-pip

ADD https://dl.eff.org/certbot-auto /tmp/.
WORKDIR /tmp
RUN chmod 700 certbot-auto
RUN ./certbot-auto -q

