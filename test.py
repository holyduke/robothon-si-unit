from orchestrator import *
from datareader.csvreader import Csvreader 
from preprocessor import Preprocessor
from searcher.searcher import create_index, add_documents, search

csv_reader = Csvreader("data/")
alza = csv_reader.parse_csv("alza.csv")
mall = csv_reader.parse_csv("mall.csv")
preprocessor = Preprocessor()
preprocessor.preprocess_data(alza.products)
preprocessor.preprocess_data(mall.products)

alza_ix = create_index('alza')
alza_ix
mall_ix = create_index('mall')
mall_ix

add_documents(alza_ix, alza.products)
add_documents(mall_ix, mall.products)

compare_eshops(alza, alza_ix, mall, mall_ix)