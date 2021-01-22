from .Product import Product

class Eshop:
  def __init__(self, name):
    self.name = name
    self.products = []

  def addProduct(self, product_row):
    self.products.append(Product(product_row[3], product_row[5]))
  
