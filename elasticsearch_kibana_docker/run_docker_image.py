#!/usr/bin/env python

''' Script to manage elasticsearch docker image.
	leverages scriptine to ease the use of cli '''

from config import mapping,docker_run,bulk_index,cluster_health,image
from scriptine import run, shell
import json
import time

__author__ = 'alcedok'

def stop_remove_images():
	shell.sh('docker stop $(docker ps -a -q)')
	shell.sh('docker rm $(docker ps -a -q)')

def check_status_command():
	indices = shell.backtick(cluster_health)

	# check health status by parsing output
	if len(indices) > 0:
		health_output = json.loads(indices)['status']
		print "\nCluster health: ",health_output
		return True
	else: 
		print "\nError: Check connection"
		return False


def start_command(image_name=image):

    # NOTE: this will start an image and remove other images running
    running_imgs = shell.backtick('docker ps')

    # if there are any images running remove them
    if len([val for val in running_imgs.splitlines()]) > 1:
    	stop_remove_images()

	# run docker image
    shell.sh(docker_run+' '+image_name)


def map_command(mapping=mapping):
    shell.sh(mapping)


def bulk_command(bulk_index = bulk_index):
	shell.sh(bulk_index)


def rundemo_command(wait = 20):
	start_command()
	flag = True

	while flag:
		if check_status_command():
			map_command()
			bulk_command() 
			flag = False
		else: 
			time.sleep(wait)


if __name__ == '__main__':
	run()