# TODO: Freeze version and automate versions update
FROM python:3.8-slim

# Make sure we don't get notifications we can't answer during building.
ENV DEBIAN_FRONTEND noninteractive

#
# Default config
#
RUN groupadd -g 9999 dev \
    && useradd -m -r -u 9999 -g dev dev

#
# Add module and packages
# TODO: Freeze versions and automate versions update
#
COPY .dependencies /opt/dependencies
RUN apt-get update \
    && for PACKAGE in `cat /opt/dependencies/container/packages.txt`; do apt-get install -y "${PACKAGE}"; done \
    && apt-get clean

USER dev

RUN /opt/dependencies/setup.sh

# TODO: Remove hard-coded values
ENV PATH="/home/dev/.local/bin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV PYTHONPATH="/workspaces/pykex/src"