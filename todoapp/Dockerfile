FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python3-dev libmysqlclient-dev nodejs

EXPOSE 8000

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install --upgrade -r requirements.txt

WORKDIR /todoapp

RUN npm install

#CMD [ "python3", "manage.py", "runserver" ]
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

ENTRYPOINT ["npm"]
CMD ["run", "serve"]