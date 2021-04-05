FROM ubuntu:20.04

RUN \
    apt-get update \
    && TZ=Europe/Paris DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        cmake \
        g++ \
        make \
        ninja-build \
        python3 \
        python3-pip \
        python3-venv \
        qt5-default \
        qtbase5-dev

RUN pip3 install --upgrade pip

COPY *requirements.txt /root/
RUN pip3 install -r /root/dev-requirements.txt

ENTRYPOINT ["/bin/bash"]
