FROM python:3.7-buster
RUN apt update -qq \
  && apt install -y --no-install-recommends \
    python-autopep8 \
    libopenblas-dev \
    liblapack-dev \
    gfortran
RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
