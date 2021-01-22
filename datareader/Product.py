import json
from ftfy import fix_encoding

class Product:
  def __init__(self, url, id, json):
    self.url = url
    self.id = id
    self.data = json

  @staticmethod
  def has_valid_data(json_str):
    json_obj = json.loads(fix_encoding(json_str))
    return json_obj if 'name' in json_obj else None



