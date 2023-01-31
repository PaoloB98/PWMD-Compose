ARG VERSION=1

FROM ubuntu:22.04

ARG VERSION

###
# For a list of pre-defined annotation keys and value types see:
# https://github.com/opencontainers/image-spec/blob/master/annotations.md
#
# Note: Additional labels are added by the build workflow.
###
LABEL org.opencontainers.image.authors="paolobono98@gmail.com"


RUN apt-get update --quiet --quiet \
    && apt-get upgrade --quiet --quiet

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes rsyslog
CMD ["sh", "-c", "service rsyslog start ; tail -f /dev/null"]
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install --quiet --yes ca-certificates mailutils \
    && apt-get --quiet --quiet clean \
    && rm --recursive --force /var/lib/apt/listsdock/* /tmp/* /var/tmp/*
COPY main.cf /etc/postfix/main.cf
COPY virtusertable /etc/postfix/virtusertable
RUN postmap /etc/postfix/virtusertable
RUN postconf maillog_file=/var/log/postfix.log
RUN cp /etc/host.conf /var/spool/postfix/etc/
RUN cp /etc/resolv.conf /var/spool/postfix/etc/
RUN cp /etc/services /var/spool/postfix/etc/


USER root
WORKDIR /root

###
# Prepare to run
###
EXPOSE 25/TCP 587/TCP
CMD ["postfix", "-v", "start-fg"]