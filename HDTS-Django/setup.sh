#!/bin/bash

sudo docker build . -t hdts:latest
sudo docker-compose up -d