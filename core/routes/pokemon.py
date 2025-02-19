from flask import request
from flask_restful import Resource
from core.predict.pokemon.predict import run_predict
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class Pokemon(Resource):
    def post(self):
        if 'file' not in request.files:
            return {"message": "Nenhum arquivo enviado"}, 400
        
        file = request.files['file']
        
        if file.filename == '':
            return {"message": "Nome do arquivo inválido"}, 400
        
        filepath = os.path.join(UPLOAD_FOLDER, "pokemon_target.jpeg")
        file.save(filepath)

        predict = run_predict(filepath)

        return {"predict": predict}, 200