FROM centos:7
ENV container docker
RUN yum update -y
RUN yum install --assumeyes python3 bash openssh-clients net-tools \
    && yum install -y --setopt=tsflags=nodocs python3-pip libstdc++ \
    && yum install -y libsctp-dev libsctp1 lksctp-tools

COPY server.py /server.py

RUN pip3 --no-cache-dir install -U pip \
    && python3 -m pip install pysctp

RUN useradd -s /bin/bash valjean
USER valjean

EXPOSE 9090
ENTRYPOINT ["/server.py"]
