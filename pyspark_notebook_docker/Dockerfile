FROM ubuntu:14.04
MAINTAINER Kevin Alcedo

USER root

## Setup for running behind proxy
#RUN echo 'Acquire::http::proxy "http://proxy.company.com:80";' >> /etc/apt/apt.conf.d/01proxy
#ENV http_proxy http://proxy.company.com:80
#ENV https_proxy http://proxy.company.com:80

## Download OS/Container dependencies
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y build-essential curl openjdk-7-jre-headless python-pip python-dev nano wget && apt-get clean


## JUPYTER NOTEBOOK 
# Download and install jupyter 
RUN pip install jupyter

## SPARK 
ENV APACHE_SPARK_VERSION 2.1.0
ENV HADOOP_VERSION 2.7

#Download pre-compiled Apache Spark 
RUN wget -qO - http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark 

## Set up environment variables
ENV DEFAULT_USER test_user
ENV HOME /home/$DEFAULT_USER
ENV SPARK_HOME /usr/local/spark
ENV PYSPARK_PYTHON /usr/bin/python
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/ipython
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# Ports to expose
EXPOSE 8888
EXPOSE 4040

# create default user and home directory
RUN useradd --create-home --home-dir /home/$DEFAULT_USER --shell /bin/bash $DEFAULT_USER 
RUN adduser $DEFAULT_USER sudo

# Start container session with default user and default home directory
USER $DEFAULT_USER 
RUN mkdir -p /home/$DEFAULT_USER/notebooks
# create a shared volume for notebooks, scripts and data 
VOLUME /home/$DEFAULT_USER/notebooks/
WORKDIR /home/$DEFAULT_USER

CMD jupyter notebook --no-browser --ip=0.0.0.0 --NotebookApp.token='test'