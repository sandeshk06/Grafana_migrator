FROM ubuntu:18.04
MAINTAINER Sandesh Kulkarni  
RUN  apt-get update \
     && apt-get install -y --no-install-recommends curl gcc  make python3 python3-pip netcat\
     && curl -sL https://deb.nodesource.com/setup_15.x | bash - \
     && apt-get install -y nodejs \
     && rm -rf /var/lib/apt/lists/* 

RUN  node -v && npm -v && npm install -g wizzy
RUN  export NODE_TLS_REJECT_UNAUTHORIZED=0
RUN  mkdir -p /opt/Grafana-backup
RUN  python3 -m pip install --upgrade pip && python3 -m pip install setuptools && python3 -m pip install bcolors
WORKDIR /opt/Grafana-backup
COPY backup_config.py .
COPY grafana_migration.py .
RUN wizzy init
RUN export PYTHONIOENCODING=utf-8
RUN chmod 755 grafana_migration.py
ENTRYPOINT ["python3","./grafana_migration.py"]
