#!/bin/bash
for url in `cat link.txt | tr "," " "`;
do
    	wget $url
	sleep 7
done
