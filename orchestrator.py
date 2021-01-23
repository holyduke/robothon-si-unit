from searcher.searcher import create_index, add_documents, search
from sku_matches import *

def get_props(product):
    return {
        "name": product.data['key_name'],
        "numbers": product.data['key_numbers'],
        "strings": product.data['key_words']
    }

def compare_eshops(one, one_ix, two, two_ix):
    num_of_matches = 0
    for product1 in one.products:
        # search product from eshop 1 in eshop 2
        print('----------\nsearching for: ' + product1.data['name'])
        result2 = search(two_ix, get_props(product1))
        # search the found product form eshop 2 again in eshop 1
        product2 = two.products[result2[1]]
        print('found: ' + product2.data['name'])
        result1 = search(one_ix, get_props(product2))
        product1_again = one.products[result1[1]]
        print('which in turn found: ' + product1_again.data['name'])
        if product1.id == product1_again.id:
            print('yay, found match!')
            num_of_matches += 1
            print('conf. value 1: ' + str(round(result1[0], 2)))
            print('conf. value 2: ' + str(round(result2[0], 2)))
        else:
            print('match not found')


