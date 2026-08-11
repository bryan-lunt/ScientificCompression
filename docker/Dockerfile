FROM alpine:latest

RUN apk --no-cache add \
    vim \
    git \
    make \
    cmake \
    build-base binutils

    #\
    #llvm22 llvm22-libs llvm22-linker-tools llvm22-static \
    #lld22 lld22-libs \
    #clang clang22-extra-tools

RUN apk add python3 py3-pip py3-pip-tools py3-pip-bash-completion py3-numpy py3-scipy
RUN apk add zip

RUN apk add bash
