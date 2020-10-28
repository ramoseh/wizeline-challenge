# Fast API
from fastapi import FastAPI, Response, Depends, BackgroundTasks, logger
import json
import uvicorn
import sqlalchemy
import datetime

# # Requests
# import client.apiClient as bitsoApi

# Routes
from routes import table, weather

# # Validation
from utils.bodies import User
# from utils.validation import rippleRequets

# Database
from db import models
from db.database import engine
from db.models import UsersTable

models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)


@app.get("/health")
def health_check():
    data = {"payload": "OK"}
    return Response(json.dumps(data), status_code=200)


@app.get("/hello")
def hello_world():
    data = {"payload": "Hello World!"}
    return Response(json.dumps(data), status_code=200)


@app.get("/table")
def get_table():
    data = table.get_table()
    return Response(json.dumps(data), status_code=200)


@app.post("/table")
def post_table(user: User):
    data = table.post_table(user.name, user.email)
    return Response(json.dumps(data), status_code=200)


@app.get("/weather")
def get_weather():
    data = weather.get_gdl_wheather()
    print(data)
    return Response(json.dumps(data), status_code=200)
