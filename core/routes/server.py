from flask import Flask
from flask_restful import Api
from .pokemon import Pokemon
from enum import Enum
from flask_cors import CORS
from .route import route

class ServerConfig(Enum):
  HOST = "0.0.0.0"
  PORT = 5000

app = Flask(__name__)
api = Api(app)

CORS(app)

def prepareRoutes():
  route_list = ["pokemon"]

  for item in route_list:
    controller = route[item]["controller"]
    path = route[item]["path"]
    
    api.add_resource(controller, path)

prepareRoutes();