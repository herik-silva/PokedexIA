from flask import Flask, request
from flask_restful import Resource, Api
from model import run_predict
import io, base64
from PIL import Image
import os

# Assuming base64_str is the string value without 'data:image/jpeg;base64,'


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
        print(predict)


        return {"predict": predict}, 200

# class Pokemon(Resource):
#     def post(self):
#         file_name = "my-image.jpeg"
#         args = parser.parse_args()
#         img = Image.open(io.BytesIO(base64.decodebytes(bytes(args['image'], "utf-8"))))
#         print(args['image'])
#         img.save(f'../{file_name}')

#         predict = run_predict(f"../{file_name}")

#         return {'predict': predict}
