FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings

RUN python -m pip install --upgrade pip

RUN mkdir /mortgage_service
RUN mkdir /mortgage_service/static
RUN mkdir /mortgage_service/media

WORKDIR /mortgage_service

ADD requirements.txt /mortgage_service

RUN pip install -r requirements.txt
ADD mortgage_platform /mortgage_service
ADD nginx /mortgage_service
