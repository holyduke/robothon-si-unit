import json
from ftfy import fix_encoding

class Product:
  def __init__(self, url, id, ugly_json):
    self.url = url
    self.id = id
    self.json_string = fix_encoding(ugly_json)
    self.data = json.loads(self.json_string)
