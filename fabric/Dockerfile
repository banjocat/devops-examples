FROM python:2

RUN pip install fabric

RUN mkdir -p /fabric

WORKDIR /fabric

COPY ./requirements.txt /fabric/requirements.txt
RUN pip install -r /fabric/requirements.txt
COPY ./fabfile.py /fabric/fabfile.py
ENV FAB help
CMD fab $FAB
