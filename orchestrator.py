from .searcher.searcher import create_index, add_documents, search
from extract_words import 

def get_props(product):
    return {
        "name": product.data['key_name'],
        "numbers": product.data['key_numbers'],
        "strings": product.data['key_words']
    }

def compare_eshops(one, one_idx, two, two_idx):
    num_of_matches = 0
    for product in one.products:
        # search product from eshop 1 in eshop 2
        result2 = search(two_idx, get_props(product))
        # search the found product form eshop 2 again in eshop 1
        result1 = search(one_idx, get_props(two[result2[0]]))
        if product.id == result1[0]:
            print('yay, found match!')
            num_of_matches += 1
        else:
            print('match not found')


