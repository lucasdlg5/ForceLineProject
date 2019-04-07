#!/bin/sh
sudo docker forceline
sudo rm forceline
git pull
sudo docker login -u "forcelinerobot" -p "789456qwe"
sudo docker build -t forcelineproject:latest .
sudo docker run -d --name forceline --restart=always -p 8000:8000 forcelineproject:latest