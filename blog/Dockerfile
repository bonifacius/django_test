FROM python:3.8-slim

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install -U pip

RUN mkdir /app
WORKDIR /app

COPY devops/infra_requirements.txt /app/devops/infra_requirements.txt
RUN pip3 install -r /app/devops/infra_requirements.txt


COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

ADD . /app/

COPY devops/cherry.py /app/cherry.py

RUN python manage.py collectstatic --no-input

CMD ['/bin/sh', '-c', 'python ../devops/cherry.py']
