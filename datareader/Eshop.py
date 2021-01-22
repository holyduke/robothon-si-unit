from .Product import Product

class Eshop:
  def __init__(self, name):
    self.name = name
    self.products = []

  def addProduct(self, product_row):
    json_obj = Product.has_valid_data(product_row[5])
    if json_obj is not None:  #product data is valid
      self.products.append(Product(product_row[3], product_row[2], json_obj))
  
