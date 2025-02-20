import gdown
import os

def downloadModelFile():
    file_id_list = {
        "pokemon_model": ["1H8a9GjCIyILohF1NQxPLuupRqw_Jl5WA", "core/cnn/pokemon/"]
    }

    for key, value in file_id_list.items():
        file_id = value[0]
        save_dir = value[1]
        save_path = os.path.join(save_dir, f"{key}.pth")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if not os.path.exists(save_path):
            url = f"https://drive.google.com/uc?export=download&id={file_id}"
            print(f"Downloading {key} from {url}...")
            gdown.download(url, save_path, quiet=False)
