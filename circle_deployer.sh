#!/bin/sh
git pull
docker build -t forceline:latest .
docker run -d --name forceline --restart=always -p 8000:8000 forceline:latest