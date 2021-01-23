
from preprocessor import Preprocessor
from loadDataSets import loadDataSets

USE_PICKLE = True

def main():
    czc, alza, mironet, mall = loadDataSets(USE_PICKLE)    

    preprocessor = Preprocessor()
    # fckng_mega_shop = [*czc.products, *alza.products,
    #                    *mironet.products,  *mall.products]
    fckng_mega_shop = [*alza.products, *mironet.products]
    # fckng_mega_shop = [fckng_mega_shop]
    preprocessor.preprocess_data(fckng_mega_shop)


if __name__ == '__main__':
    main()
