FROM python:3.7-alpine

RUN apk add gcc pcre pcre-dev musl-dev linux-headers jpeg-dev zlib-dev postgresql-dev && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY config/ config/
COPY app/ app/
COPY static/ static/
RUN chmod -R 777 static/
COPY *.py ./

EXPOSE 8000/tcp
#CMD ["uwsgi", "--http", ":8000", "--wsgi-file", "config/wsgi.py"]
