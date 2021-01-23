from searcher.searcher import create_index, add_documents, search
from sku_matches import *

def get_props(product):
    return {
        "name": product.data['key_name'],
        "numbers": product.data['key_numbers'],
        "strings": product.data['key_words']
    }

def match_duplicites(eshop, eshop_ix):
    num_of_duplicites = 0
    for product in eshop.products:
        results = search(eshop_ix, get_props(product), 3)
        for result in results:
            if result[0] <= 0.99:
                continue
            product_again = eshop.products[result[1]]
            if product_again.id == product.id:
                continue
            if len(product.data['duplicates']) == 0 and len(product.data['duplicates']) == 0:
                num_of_duplicites += 1
            product.data['duplicates'].add(product_again.id)
            #print('Found duplicate! ' + product.data['name'] + ' == ' + product_again.data['name'])
            #print(product.url + ' == ' + product_again.url)
            if len(product.data['duplicates']) >= 3:
                print('------------------OSHRIRIRIT---------------------')

    print('Found ' + str(num_of_duplicites) + ' duplicates in ' + str(len(eshop.products)) + ' items')
    


def compare_eshops(one, one_ix, two, two_ix):
    num_of_matches = 0
    for product1 in one.products:
        # search product from eshop 1 in eshop 2
        print('----------\nsearching for: ' + product1.data['name'])
        result2 = search(two_ix, get_props(product1), 1)[0]
        if(result2[0] == 0):
            print('no match at all')
            continue
        # search the found product form eshop 2 again in eshop 1
        product2 = two.products[result2[1]]
        #print('found: ' + product2.data['name'])
        result1 = search(one_ix, get_props(product2), 1)[0]
        product1_again = one.products[result1[1]]
        #print('which in turn found: ' + product1_again.data['name'])
        if product1.id in [product1_again.id, *product1_again.data['duplicates']]:
            print('yay, found match!')
            print(product1.data['name'] + " == " + product2.data['name'])
            num_of_matches += 1
            print('conf. value 1: ' + str(round(result1[0], 2)))
            print('conf. value 2: ' + str(round(result2[0], 2)))
        else:
            print('match not found')
    print('Matched: ' + str(num_of_matches) + ' of ' + str(len(one.products)))

