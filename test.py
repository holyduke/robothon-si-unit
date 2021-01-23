from orchestrator import *
from loadDataSets import loadDataSets
from preprocessor import Preprocessor
from searcher.searcher import create_index, add_documents, search

czc, alza, mironet, mall = loadDataSets(True)
preprocessor = Preprocessor()
preprocessor.preprocess_data(alza.products)
preprocessor.preprocess_data(mall.products)

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

# print('alza duplicates:')
# match_duplicites(alza, alza_ix)
# print('mall duplicates:')
# match_duplicites(mall, mall_ix)
print('czc duplicates:')
match_duplicites(czc, czc_ix)
print('mironet duplicates:')
match_duplicites(mironet, mironet_ix)
#compare_eshops(mall, mall_ix, alza, alza_ix)