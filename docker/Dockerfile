FROM alpine:3.11

# VERSIONS
ENV ALPINE_VERSION=3.11 \
    PYTHON_VERSION=2.7.18

RUN apk --no-cache add \
    vim \
    git \
    make \
    cmake \
    build-base binutils

RUN apk add zip
RUN apk add bash

RUN apk add python2 python2-dev py2-pip openblas-dev
RUN pip install numpy==1.16
# RUN pip install scipy==1.2.3
