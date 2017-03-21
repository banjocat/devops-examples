FROM nginx:stable

RUN apt-get update -y && apt-get install -y \
        python-pip

ADD https://dl.eff.org/certbot-auto /tmp/.
WORKDIR /tmp
RUN chmod 700 certbot-auto
# False failure here
RUN test $(./certbot-auto -q) -eq 1





