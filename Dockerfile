FROM python:3.10-slim

RUN mkdir -p /srv/docker

WORKDIR /srv/docker/

COPY ./ ./

# RUN chmod 755 .

RUN apt-get update && apt-get full-upgrade -y\
    && pip install -r requirements.txt\
    && apt autoclean && apt autoremove -y

ENV TZ Europe/Moscow

EXPOSE 80
EXPOSE 443

CMD python3 main.py