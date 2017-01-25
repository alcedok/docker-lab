## Docker Elasticsearch Kibana 
<p align="center"><img src= "https://raw.githubusercontent.com/alcedok/docker-lab/master/elasticsearch_kibana_docker/images/logos.png" width="282" height="240"></p>

### Summary

Launch an Elasticsearch (ES) & Kibana (K) instance quickly and effortlessly with Docker. I've also included a sample python script that can help you load json files in bulk to ES.

### Notes
Docker container installs/runs Elasticsearch-2.4.1 and Kibana-4.6.1 on Ubuntu-14.04. 

When ran with *run_docker_image.py* ES and K are mapped to be on the native ports on both container and local (of course this can be changed in the *config.py*) . 

**Handling HTTP-Proxies**:
 - Within the Dockerfile you will find a commented section that can be edited if you will be running this behind a corporate proxy.

### How to
*assuming docker is installed*

To build: 

    docker build -t alcedok/elasticsearch_kibana_ubuntu .
 

### Requirements

 - Docker-1.12.3-beta30

 - python 2.7.10
	- [scriptine-0.2.1](https://pypi.python.org/pypi/scriptine) ( if using the python script utility)
	- pandas-0.19.0 (if using the data preprocessing example)


## Example
##### The following example uses a dataset of airports around the world to show how this container set can be used for data exploration and profiling


Lets say we have a dataset of airports around the world and we wanted to do some quick profiling and visualizations through the Kibana dashboard, while leveraging Elasticsearch. The data comes in the form of a csv, with 50,046 airports with 6 features. We'll only focus on the "large airports"; which gives us 570 airports total. 

Further filtering and preprocessing is done to form a json file that can be parsed in bulk by elasticsearch. This can be accomplished by running the preprocessing script found in the *data_preprocessing* folder.

    python preprocessing
 With our data processed we are then ready to run start our docker image assuming its already built/pulled locally. 
 

    python run_docker_image rundemo
   
  This will go through the process of removing any running images, the starting a new instance. After elasticsearch index is ready mapping is added (found in *config.py*) and the data is bulk inserted. 

Now we can do some exploration and visualizations with Kibana. In your browser go to *http://localhost:5601/*. 

Below is an example dashboard:

 - Tile map of  all large airports
 - Tile map of a range query on airports near NYC
 - Table of the airport's wiki page sorted by their elevation
 - Total count of airports


<img src= "https://raw.githubusercontent.com/alcedok/docker-lab/master/elasticsearch_kibana_docker/images/dashboard.png">
