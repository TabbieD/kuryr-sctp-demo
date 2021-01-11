FROM centos:8
LABEL author="Tabitha Fasoyin<fifedolapo02@gmail.com>"
ENV container docker

RUN yum update -y \
    && yum install -y epel-release \
    && yum install -y python3 bash openssh-clients net-tools \
    && yum install -y --setopt=tsflags=nodocs python3-pip libstdc++ \
    && yum install -y --setopt=tsflags=nodocs gcc gcc-c++ python3-devel \
    && yum install -y lksctp-tools lksctp-tools-devel

COPY server.py /server.py

RUN pip3 --no-cache-dir install -U pip \
    && python3 -m pip install pysctp

RUN chmod +x /server.py

EXPOSE 9090
ENTRYPOINT ["/server.py"]
