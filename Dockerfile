FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
