#!/bin/bash

docker run \
    --rm \
    -it \
    --net=host \
    weather-app:latest 