import os
import torch
from torchvision import transforms
from PIL import Image
import json

from ...cnn.pokemon.cnn import PokemonCNN

model = PokemonCNN()

def predict(image_path, model, class_names, device):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    
    image = image.to(device)
    model = model.to(device)
    
    model.eval()
    
    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
    return class_names[predicted_class], probabilities[0][predicted_class].item()

def run_predict(image_path):
    file_path = "core/predict/pokemon/pokemon_list.json"
    with open(file_path, "r") as file:
        class_names = json.load(file)

    print(os.path.abspath("./core/cnn/pokemon/pokemon_modelv2.pth"))
    absolute_path = os.path.abspath("./core/cnn/pokemon/pokemon_model.pth")
    model.load_state_dict(torch.load(absolute_path, map_location="cpu"))

    predicted_class, _ = predict(image_path, model, class_names, "cpu")

    return predicted_class