from flask import Flask
from flask_restful import Api
from routes.pokemon import Pokemon
from enum import Enum

class ServerConfig(Enum):
  HOST = "0.0.0.0"
  PORT = 5000

app = Flask(__name__)
api = Api(app)

api.add_resource(Pokemon, '/pokemon')

if __name__ == '__main__':
    app.run(debug=True, host=ServerConfig.HOST.value, port=ServerConfig.PORT.value)