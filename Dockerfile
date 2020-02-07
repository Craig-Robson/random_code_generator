FROM ubuntu:18.04
ADD run.py /home
COPY code_generator /code_generator
WORKDIR /home
RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && pip3 install -r /code_generator/requirements.txt
    