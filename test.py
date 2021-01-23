from orchestrator import *
from loadDataSets import loadDataSets
from preprocessor import Preprocessor
from searcher.searcher import create_index, add_documents, search

czc, alza, mironet, mall = loadDataSets(True)
preprocessor = Preprocessor()
preprocessor.preprocess_data(alza.products)
preprocessor.preprocess_data(mall.products)

alza_ix = create_index('alza')
alza_ix
mall_ix = create_index('mall')
mall_ix

add_documents(alza_ix, alza.products)
add_documents(mall_ix, mall.products)

print('alza duplicates:')
match_duplicites(alza, alza_ix)
print('mall duplicates:')
match_duplicites(mall, mall_ix)
compare_eshops(alza, alza_ix, mall, mall_ix)