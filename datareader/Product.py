import json
import unicodedata
from ftfy import fix_encoding


class Product:
    def __init__(self, url, id, json_obj):
        self.url = url
        self.id = id
        self.data = json_obj

    @staticmethod
    def has_valid_data(json_str):
        json_str = json_str.lower()
        json_str = fix_encoding(json_str)        
        nfkd_form = unicodedata.normalize('NFKD', json_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        jsonobj = json.loads(only_ascii)
        if 'name' in jsonobj.keys() and 'additionalproperty' in jsonobj.keys():
          return jsonobj
        else:
          return None
