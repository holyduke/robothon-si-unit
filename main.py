
from datareader.csvreader import Csvreader 
from preprocessor import Preprocessor

def main():
    csv_reader = Csvreader("data/")
    # czc = csv_reader.parse_csv("czc.csv")
    alza = csv_reader.parse_csv("alza.csv")
    # mironet = csv_reader.parse_csv("mironet.csv")
    # mall = csv_reader.parse_csv("mall.csv")

    preprocessor = Preprocessor()
    # fckng_mega_shop = [*czc.products, *alza.products, *mironet.products,  *mironet.products]
    fckng_mega_shop = [*alza.products]
    preprocessor.preprocess_data(fckng_mega_shop)

    
if __name__ == '__main__':
    main()