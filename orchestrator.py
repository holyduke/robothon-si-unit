from searcher.searcher import create_index, add_documents, search
from sku_matches import *
import re

def get_props(product):
    return {
        "name": product.data['key_name'],
        "numbers": product.data['key_numbers'],
        "strings": product.data['key_words']
    }

def match_duplicites(eshop, eshop_ix):
    num_of_duplicites = 0
    for product in eshop.products:
        results = search(eshop_ix, get_props(product), 5, use_what=['name'])
        for result in results:
            if result[0] < .9:
                continue
            product_again = eshop.products[result[1]]
            if product_again.id == product.id:
                continue
            number_set_original = set(re.findall(r"(\w*\d+\w*\d*)", product.data['name']))
            number_set_again = set(re.findall(r"(\w*\d+\w*\d*)", product_again.data['name']))
            if (len(number_set_original-number_set_again) != 0 or len(number_set_again-number_set_original) != 0):
                continue
            if len(product.data['duplicates']) == 0 and len(product_again.data['duplicates']) == 0:
                num_of_duplicites += 1
            product.data['duplicates'].add(product_again.id)
            product_again.data['duplicates'].add(product.id)
            #print('Found duplicate! ' + product.data['name'] + ' == ' + product_again.data['name'])
            #print(product.url + ' == ' + product_again.url)

    print('Found ' + str(num_of_duplicites) + ' duplicates in ' + str(len(eshop.products)) + ' items')
    


def compare_eshops(one, one_ix, two, two_ix):
    num_of_matches = 0
    for product1 in one.products:
        # search product from eshop 1 in eshop 2
        #print('----------\nsearching for: ' + product1.data['name'])
        result2 = search(two_ix, get_props(product1), 1, use_what=['name'])
        if(len(result2) == 0):
            print('no match at all')
            continue
        # search the found product form eshop 2 again in eshop 1
        product2 = two.products[result2[0][1]]
        #print('found: ' + product2.data['name'])
        result1 = search(one_ix, get_props(product2), 1, use_what=['name'])
        if(len(result1) == 0):
            print('no reverse match')
            continue
        number_set_1 = set(re.findall(r"(\w*\d+\w*\d*)", product1.data['name']))
        number_set_2 = set(re.findall(r"(\w*\d+\w*\d*)", product2.data['name']))
        if (len(number_set_1-number_set_2) > 1 or len(number_set_2-number_set_1) > 1):
            print('numbers don\'t match')
            continue
        product1_again = one.products[result1[0][1]]
        #print('which in turn found: ' + product1_again.data['name'])
        if product1.id in [product1_again.id, *product1_again.data['duplicates']]:
            #print('yay, found match!')
            print(product1.data['name'] + " == " + product2.data['name'])
            product1.data['similar_listings'][two.name] = product2.id
            num_of_matches += 1
            #print('conf. value 1: ' + str(round(result1[0][0], 2)))
            #print('conf. value 2: ' + str(round(result2[0][0], 2)))
        else:
            print('match not found')
    print('Matched: ' + str(num_of_matches) + ' of ' + str(len(one.products)))

