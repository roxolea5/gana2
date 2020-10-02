FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /g2app

ENV gana2_host 192.168.56.101
ENV gana2_db rancho_dev
ENV FLASK_ENV development

COPY . /g2app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "webserver.py"]