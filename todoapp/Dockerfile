FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python3-dev libmysqlclient-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install --upgrade -r requirements.txt

COPY . /

ENTRYPOINT [ "ngrok" ]
CMD [ "http -region=us -hostname=kevinmikio.ngrok.io 8000 > /dev/null &" ]

ENTRYPOINT [ "python3" ]
CMD [ "manage.py runserver" ]
