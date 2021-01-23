import json
import unicodedata
from ftfy import fix_encoding


class Product:
    def __init__(self, url, id, json_str):
        self.url = url
        self.id = id
        nfkd_form = unicodedata.normalize('NFKD', json_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        self.data = json.loads(only_ascii)

    @staticmethod
    def has_valid_data(json_str):
        json_str = json_str.lower()
        json_str = fix_encoding(json_str)        
        if not 'additionalproperty' in json_str:
          return None
        return json_str if 'name' in json_str else None
