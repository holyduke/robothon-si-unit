
from preprocessor import Preprocessor
from loadDataSets import loadDataSets
from dataExport import dataExport

USE_PICKLE = True

def main():
    czc, alza, mironet, mall = loadDataSets(USE_PICKLE)    

    preprocessor = Preprocessor()
    # fckng_mega_shop = [*czc.products, *alza.products,
    #                    *mironet.products,  *mall.products]
    fckng_mega_shop = [*alza.products, *mironet.products]
    # fckng_mega_shop = [fckng_mega_shop]
    preprocessor.preprocess_data(fckng_mega_shop)

    eshops = {
        'alza':[
            {
                'id': 8,
                'url': 'string',
                'data': {
                    'name': "Hodinky",
                    'description': "Hodinky",
                    'brand': "znacka",
                    'price': "cena",
                    'duplicates': [1, 5, 7],
                    'similar_listings': {
                        'mall': 'we85',
                        'czc': 'efeš',
                        'mironet':  '8787'
                    },
                }
            },
            {
                'id': 9,
                'url': 'https://stackoverflow.com/questions/45565349/how-to-acces-external-json-file-objects-in-vue-js-app',
                'data': {
                    'name': "Notebook toshiuba",
                    'description': "popis",
                    'brand': "znacka",
                    'price': "cena",
                    'duplicates': [1, 5, 7],
                    'similar_listings': {
                        'mall': 'we85',
                        'czc': 'efeš',
                        'mironet':  '8787',
                    }
                }
            }
        ],
        'czc':[
            {
                'id': 8,
                'url': 'https://stackoverflow.com/questions/45565349/how-to-acces-external-json-file-objects-in-vue-js-app',
                'data': {
                    'name': "TV LG",
                    'description': "popis",
                    'brand': "znacka",
                    'price': "cena",
                    'duplicates': [1, 5, 7],
                    'similar_listings': {
                        'mall': 'we85',
                        'czc': 'efeš',
                        'mironet':  '8787'
                    },
                }
            },
            {
                'id': 9,
                'url': 'https://stackoverflow.com/questions/45565349/how-to-acces-external-json-file-objects-in-vue-js-app',
                'data': {
                    'name': "Notebook Apple",
                    'description': "popis",
                    'brand': "znacka",
                    'price': "cena",
                    'duplicates': [1, 5, 7],
                    'similar_listings': {
                        'mall': 'we85',
                        'czc': 'efeš',
                        'mironet':  '8787',
                    }
                }
            }
        ]
    }
    
    dataExport(eshops)


if __name__ == '__main__':
    main()
