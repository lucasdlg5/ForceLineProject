FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python3-dev libmysqlclient-dev

EXPOSE 8000

COPY ./requirements.txt /requirements.txt

WORKDIR /todoapp

RUN pip3 install --upgrade -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver" ]
