def is_products_match(product1, product2):
  ids = []
  if "sku" in product1.data:
    ids.append(product1.data['sku'])
  if "mpn" in product1.data:
    ids.append(product1.data['mpn'])
  if "sku" in product2.data:
    ids.append(product2.data['sku'])
  if "mpn" in product2.data:
    ids.append(product2.data['mpn'])
  return len(ids) != len(set(ids))

def is_sku_match(product, sku):
  ids = [sku]
  if "sku" in product.data:
    ids.append(product.data['sku'])
  if "mpn" in product.data:
    ids.append(product.data['mpn'])
  return len(ids) != len(set(ids))

def find_matches_by_target(products, target_product):
  matches = [target_product]
  for product in products:
    if is_products_match(product, target_product):
      matches.append(product)
  return matches

def find_matches_by_sku(products, sku):
  matches = []
  for product in products:
    if is_sku_match(product, sku):
      matches.append(product)
      
  return matches

# shop_matches = []
# for product in czc.products:
#     matches = find_matches_by_target(alza.products, product)
#     if len(matches)>1:
#         shop_matches.append(matches)