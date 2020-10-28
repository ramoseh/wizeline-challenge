FROM alpine:3.7
RUN apk update && apk upgrade
RUN apk add --no-cache curl build-base python3 pkgconfig python3-dev openssl-dev libffi-dev musl-dev make gcc linux-headers
RUN apk add --update python3

RUN  pip3 install --upgrade pip \
    && pip3 install fastapi\
    && ln -sv /usr/bin/python3 /usr/bin/python

COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
ADD ./db /src/db
ADD ./client /src/client
ADD ./routes /src/routes
ADD ./utils /src/utils
ADD ./tests /src/tests
ADD ./app.py /src/app.py

WORKDIR /src

CMD ["uvicorn", "app:app","--host","0.0.0.0", "--port", "15400"]
