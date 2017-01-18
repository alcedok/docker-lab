# ElasticSearch + Kibana on ubuntu:14.04

FROM ubuntu:14.04
MAINTAINER Kevin Alcedo

# RUN echo 'Acquire::http::proxy "http://yourproxy.com:80";' >> /etc/apt/apt.conf.d/01proxy
# ENV http_proxy http://yourproxy.com:80
# ENV https_proxy http://yourproxy.com:80

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y curl openjdk-7-jre-headless python python-pip nano

# elasticsearch
RUN curl -fL https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.1/elasticsearch-2.4.1.tar.gz | tar xzf - -C /opt && \
mv /opt/elasticsearch-2.4.1 /opt/elasticsearch

# python elasticsearch
RUN pip install elasticsearch

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/elasticsearch/bin

# kibana

RUN curl -fL https://download.elastic.co/kibana/kibana/kibana-4.6.1-linux-x86_64.tar.gz | tar xzf - -C /opt && \
mv /opt/kibana-4.6.1-linux-x86_64 /opt/kibana

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/kibana/bin

CMD /opt/elasticsearch/bin/elasticsearch -d -Des.insecure.allow.root=true -Des.network.host=0.0.0.0 && kibana
