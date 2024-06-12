#!/bin/bash

docker stop weather-reciever 

docker run \
    --rm \
    -d \
    -u "$UID" \
    --name weather-reciever \
    --net=host \
    -v "/home/$USER/.weather-data":/data:z \
    weather-app:latest  
