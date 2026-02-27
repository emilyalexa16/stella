import os
import xmltodict

# change the xml into a python dictionary so we can navigate/access items more easily
def load_save_file(file_path: str):
# file_path = os.path.expanduser("/Users/emilygotiangco/School/cmps_490/Saves/Ivans_401983009/Ivans_401983009")
    file_path = os.path.expanduser(file_path)
    with open(file_path) as f:
        data = xmltodict.parse(f.read())
    return data