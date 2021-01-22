import re
from extract_words import _extract_words 
class Preprocessor():
    def __init__(self):
        units_length_conversions = {
            "km": 1000000,
            "m": 1000,
            "dm": 100,
            "cm": 10,
        }
        pass

    def preprocess_data(self, data):
        print(data)
        for product in data:
            product["key_numbers"] = self._extract_numbers(product)
            product["key_words"] = _extract_words(product)


    def _extract_numbers(self, product):
        numbers = []
        for ad in product.data["additionalProperty"]:
            re.match(r"[\d,\.]")
            numbers.append(ad["value"])


        return "1 2 3"