#!/bin/bash

sudo docker build . -t hdts:latest
sudo docker network create hdts_net
sudo docker-compose up -d

