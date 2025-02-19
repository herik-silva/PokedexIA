from typing import TypedDict
from flask_restful import Resource

from .pokemon import Pokemon

class RouteItem(TypedDict):
    controller: Resource
    path: str

class Route(TypedDict):
    pokemon: RouteItem

route: Route = {
    "pokemon": {
        "controller": Pokemon,
        "path": "/pokemon"
    }
}
