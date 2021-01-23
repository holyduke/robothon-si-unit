import json
from orchestrator import *
from loadDataSets import loadDataSets
from preprocessor import Preprocessor
from searcher.searcher import create_index, add_documents, search

czc, alza, mironet, mall = loadDataSets(False)
preprocessor = Preprocessor()
preprocessor.preprocess_data(alza.products)
preprocessor.preprocess_data(mall.products)
preprocessor.preprocess_data(czc.products)
preprocessor.preprocess_data(mironet.products)


print(alza.name)
print(czc.name)
print(mironet.name)
print(mall.name)


alza_ix = create_index('alza')
mall_ix = create_index('mall')
czc_ix = create_index('czc')
mironet_ix = create_index('mironet')

print('index for alza')
add_documents(alza_ix, alza.products)
print('index for mall')
add_documents(mall_ix, mall.products)
print('index for czc')
add_documents(czc_ix, czc.products)
print('index for mironet')
add_documents(mironet_ix, mironet.products)

print('alza duplicates:')
match_duplicites(alza, alza_ix)
print('mall duplicates:')
match_duplicites(mall, mall_ix)
print('czc duplicates:')
match_duplicites(czc, czc_ix)
print('mironet duplicates:')
match_duplicites(mironet, mironet_ix)


compare_eshops(alza, alza_ix, czc, czc_ix)
compare_eshops(alza, alza_ix, mironet, mironet_ix)
compare_eshops(alza, alza_ix, mall, mall_ix)

# compare_eshops(czc, czc_ix, mironet, mironet_ix)
# compare_eshops(czc, czc_ix, alza, alza_ix)
# compare_eshops(czc, czc_ix, mall, mall_ix)

# compare_eshops(mall, mall_ix, czc, czc_ix)
# compare_eshops(mall, mall_ix, alza, alza_ix)
# compare_eshops(mall, mall_ix, mironet, mironet_ix)

# compare_eshops(mironet, mironet_ix, czc, czc_ix)
# compare_eshops(mironet, mironet_ix, alza, alza_ix)
# compare_eshops(mironet, mironet_ix, mall, mall_ix)

def convert_product(product):
    return {
        "id": product.id,
        "name": product.data["name"],
        "duplicates": list(product.data["duplicates"]),
        "similar_listings": product.data["similar_listings"],
        "price": product.data['offers']['price'] if 'offers' in product.data else None,
        "url": product.url
    }


def convert_to_json(products):
    return [convert_product(product) for product in products]


data = {
    "alza": convert_to_json(alza.products),
    "czc": convert_to_json(czc.products),
    "mall": convert_to_json(mall.products),
    "mironet": convert_to_json(mironet.products)
}

with open('data/alza.json', 'w') as f:
    json.dump(data, f)