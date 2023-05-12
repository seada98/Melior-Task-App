FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add gcc python3-dev musl-dev

WORKDIR /api
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod o+x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]