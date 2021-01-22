import json
from ftfy import fix_encoding

class Product:
  def __init__(self, url, id, ugly_json):
    self.url = url
    self.id = id
    self.data = json.loads(fix_encoding(ugly_json))
