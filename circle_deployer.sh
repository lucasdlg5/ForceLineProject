#!/bin/sh
git pull
docker run -d --name forceline --restart=always -p 8000:8000 forceline:latest