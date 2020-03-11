FROM python:latest
RUN apt update -qq \
  && apt install -y --no-install-recommends \
    python-autopep8
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
