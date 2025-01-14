FROM ubuntu:20.04

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web

# Setup
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends python3 python3-dev postgresql-client postgresql-server-dev-all gettext ncbi-blast+ xvfb
RUN apt-get install -y python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libapache2-mod-wsgi-py3 binutils libproj-dev gdal-bin
RUN pip3 install --upgrade pip
COPY requirements/base.txt /data/web/
RUN pip3 install -r base.txt --ignore-installed
# Get weasyprint to work
RUN pip3 install weasyprint
RUN pip3 install --no-cache-dir --force-reinstall cffi
RUN pip3 install --no-cache-dir cairocffi

# Prepare
COPY . /data/web/

RUN apt-get update
RUN apt-get install -y samtools firefox xvfb
# Need this for GeneSeekr to work.
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

