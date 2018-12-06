# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
import json
import os
from urllib.request import urlopen
import requests
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class JsonClass:
    # ¬¬¬¬¬¬¬¬¬
    def __init__(self):
        super().__init__()
    # ¬¬¬¬¬¬¬¬¬
    def loadjsonFile(self, path_to_json):
        with open(path_to_json, "r") as read_file:
            return json.load(read_file)
    # ¬¬¬¬¬¬¬¬¬
    def saveJsonFile(self, path_to_json, dict_to_save):
        with open(path_to_json, "w") as write_file:
            json.dump(dict_to_save, write_file)
    # ¬¬¬¬¬¬¬¬¬
    def loadJsonFromOnline(self, url_to_json):
        return json.load(urlopen(url_to_json))
    # ¬¬¬¬¬¬¬¬¬
    def saveJsonOnline(self, url_to_php, dict_to_save):
        url = url_to_php
        payload = dict_to_save
        r = requests.post(url, json=payload)
    # ¬¬¬¬¬¬¬¬¬
        
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# Version 1

# from JsonClass import JsonClass
# self.jsonClassObj = JsonClass()
# dict = self.jsonClassObj.loadjsonFile(path_to_json)
# self.jsonClassObj.saveJsonFile(path_to_json, dict_to_save)
# self.jsonClassObj.loadJsonFromOnline(url_to_php, dict_to_save)
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬