import os
import xmltodict

def load_save_file(file_path: str):
    file_path = os.path.expanduser(file_path)
    with open(file_path) as f:
        data = xmltodict.parse(f.read())
    return data