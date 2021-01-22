from .Product import Product

class Eshop:
  def __init__(self, name):
    self.name = name
    self.products = []

  def addProduct(self,new_product):
    self.products.append(Product(new_product))
  
