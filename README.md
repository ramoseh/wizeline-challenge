# wizeline-challenge
This repo contains the project for the challenge in order to enter the golang bootcamp

### How to start

This project requires python 3.8 to run.

Install the dependencies and devDependencies and start the server.

```sh
$ pip install -r requirements.txt
```

Run next command to star server

```sh
$ uvicorn main:app --reload
```

### To run in Docker

After you install the dependencies

```sh
$ docker-compose up --force-recreate --build -d
$ docker image prune -f
```

### To test
After you install the dependencies
```sh
$ pytest
```
