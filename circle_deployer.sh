#!/bin/sh
git pull
sudo docker build -t forcelineproject:latest .
sudo docker run -d --name forceline --restart=always -p 8000:8000 forcelineproject:latest