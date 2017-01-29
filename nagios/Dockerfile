FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
        autoconf \
        gcc \
        libc6 \
        build-essential \
        bc \
        gawk \
        dc \
        gettext \
        libmcrypt-dev \
        libssl-dev \
        make \
        unzip \
        apache2 \
        apache2-utils \
        php5 \
        libgd2-xpm-dev \
        supervisor \
        wget

RUN useradd -m -s /bin/bash nagios
RUN usermod -G nagios nagios
RUN groupadd nagcmd
RUN usermod -a -G nagcmd nagios
RUN usermod -a -G nagcmd www-data

WORKDIR /tmp
RUN wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.2.4.tar.gz
RUN wget https://nagios-plugins.org/download/nagios-plugins-2.1.4.tar.gz

RUN tar xzf nagios-4.2.4.tar.gz
WORKDIR /tmp/nagios-4.2.4

RUN ./configure --with-command-group=nagcmd --with-httpd-conf=/etc/apache2/sites-enabled
RUN make all
RUN make install
RUN make install-init
RUN make install-config
RUN make install-commandmode
RUN update-rc.d nagios defaults

RUN make install-webconf
RUN a2enmod rewrite
RUN a2enmod cgi
RUN htpasswd -b -c /usr/local/nagios/etc/htpasswd.users nagiosadmin changeme

WORKDIR /tmp
RUN tar xzf nagios-plugins-2.1.4.tar.gz
WORKDIR /tmp/nagios-plugins-2.1.4

RUN ./configure
RUN make
RUN make install

EXPOSE 80

COPY ./nagios.ini /etc/supervisor/conf.d/nagios.conf
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY ./create_config.py /tmp/.
COPY ./objects.cfg.j2 /tmp/.
COPY ./start_up.sh /tmp/.
RUN chmod 700 /tmp/start_up.sh
RUN mkdir -p /usr/local/nagios/etc/objects/docker
RUN echo "cfg_dir=/usr/local/nagios/etc/objects/docker" >> /usr/local/nagios/etc/nagios.cfg
CMD /tmp/start_up.sh





