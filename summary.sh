#!/bin/bash

# create results folder if it doesn't exist
mkdir -p customer-analytics/results

# copy all output files from container to host
docker cp bigdata-container:/app/pipeline/data_raw.csv customer-analytics/results/
docker cp bigdata-container:/app/pipeline/data_preprocessed.csv customer-analytics/results/
docker cp bigdata-container:/app/pipeline/insight1.txt customer-analytics/results/
docker cp bigdata-container:/app/pipeline/insight2.txt customer-analytics/results/
docker cp bigdata-container:/app/pipeline/insight3.txt customer-analytics/results/
docker cp bigdata-container:/app/pipeline/summary_plot.png customer-analytics/results/
docker cp bigdata-container:/app/pipeline/clusters.txt customer-analytics/results/

echo "All files copied to customer-analytics/results/"

# stop and delete the container
docker stop bigdata-container
docker rm bigdata-container

echo "Container stopped and removed"