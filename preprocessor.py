import re
from extract_words import _extract_words


class Preprocessor():
    def __init__(self):

        self.units = {
            "length": {
                "pattern": r"km|m|cm|dm|mm|\"|\"|inch|inches",
                "default": "mm",
                "conversions": {
                    "km": 1000000,
                    "m": 1000,
                    "dm": 100,
                    "cm": 10,
                    "mm": 1,
                    "inch": 25.4,
                    '"': 25.4,
                    '"': 25.4,
                    'inches': 25.4,
                }
            },
            "weight": {
                "pattern": r"t|kg|g",
                "default": "g",
                "conversions": {
                    "t": 1_000_000,
                    "kg": 1_000,
                    "g": 1,
                }
            },
            "power": {
                "pattern": r"mw|kw|w",
                "default": "w",
                "conversions": {
                    "mw": 1_000_000,
                    "kw": 1_000,
                    "w": 1,
                }
            },
            "freq": {
                "pattern": r"hz|khz",
                "default": "hz",
                "conversions": {
                    "khz": 1_000,
                    "hz": 1,
                }
            },
            "duration": {
                "pattern": r"h|dnů|dnu|d|min|minut|minuty|s|ms|ns",
                "default": "s",
                "conversions": {
                    "dnů": 86_400,
                    "dnu": 86_400,
                    "d": 86_400,
                    "h": 3_600,
                    "min": 60,
                    "minut": 60,
                    "minuty": 60,
                    "s": 1,
                    "ms": 0.001,
                    "ns": 0.000001,
                }
            },
            "storage": {
                "pattern": r"tb|gb|mb|kb",
                "default": "mb",
                "conversions": {
                    "tb": 1_000_000,
                    "gb": 1_000,
                    "mb": 1,
                    "kb": 0.001,
                }
            },
            "power": {
                "pattern": r"kw|w",
                "default": "w",
                "conversions": {
                    "kw": 1_000,
                    "w": 1,
                }
            },
            "amperhour": {
                "pattern": r"ah|mah",
                "default": "mah",
                "conversions": {
                    "ah": 1_000,
                    "mah": 1,
                }
            },
            "others": {
                "pattern": r"ghz",
                "default": None,
                "conversions": {
                    "ghz": 1,
                }
            }
        }

        self.all_units_pattern = ""
        for key in self.units:
            self.all_units_pattern += self.units[key]["pattern"] + "|"
        self.all_units_pattern = self.all_units_pattern.strip("|")

        
        self.all_units_regex_alone = re.compile(
            r"([\(\[\{]|\s|^|\d|\b)(" + self.all_units_pattern + r")(\s|\b|$|[\)\]\}])", re.IGNORECASE)
        self.number_with_regex = re.compile(
            r"\d+[\,\.]?[\d]+(?:[\(\[\{]|\s|\d|)(?:" + self.all_units_pattern + r"|)(?:\s|\b|[\)\]\}])", re.IGNORECASE)
        self.numbers_regex = re.compile(r"\d+[\,\.]?[\d]+", re.IGNORECASE)
        self.useless_chars_regex = re.compile(r"([\(\){}\[\],])")

    def preprocess_data(self, products):
        for product in products:
            self._extract_key_features(product)

            product.data["key_name"] = product.data["name"].split()
            product.data["duplicates"] = set()
            product.data["similar_listings"] = {}

        self._remove_frequent(products)
        pass
   

    def _extract_key_features(self, product):
        product.data["key_numbers"] = set()
        product.data["key_words"] = set()

        if "additionalproperty" not in product.data.keys():
            return

        # Add key features from aditional properties
        for ad in product.data["additionalproperty"]:
            found_number = self._parse_value(ad)
            if found_number is not None:
                for num in found_number:
                    product.data["key_numbers"].add(num)
            else:
                for word in self._parse_sentence(ad["value"]):
                    product.data["key_words"].add(word)
        
        # Add key features from description
        if "description" in product.data.keys():
            words, numbers = self._parse_description(product.data["description"])
            for x in numbers:
                product.data["key_numbers"].add(x)
            for x in words:
                product.data["key_words"].add(x)


    def _parse_value(self, property):
        numbers = self.numbers_regex.findall(property["value"])
        if len(numbers) != 0:
            numbers = [number.replace(",", ".") for number in numbers]
            unit_match = self.all_units_regex_alone.search(
                property["value"], re.IGNORECASE)
            if unit_match is None:
                unit_match = self.all_units_regex_alone.search(
                    property["value"], re.IGNORECASE)
            else:
                if len(self.all_units_regex_alone.findall(property["value"], re.IGNORECASE)) > 1:
                    return None

            if unit_match is None:
                return [str(round(float(num))) for num in numbers if len(str(round(float(num)))) > 2]

            # Unit found
            numbers = [self.append_unit(number, unit_match.group(2)) for number in numbers]
            return [num for num in numbers if len(num) > 2]
                    

        else:  # number not found
            return None

    def append_unit(self, number, unit):
        for unit_key in self.units:
            if unit in self.units[unit_key]["pattern"].split("|"):
                final_string = str(round(float(number.replace(",", ".")) * self.units[unit_key]["conversions"][unit]))
                final_string += self.units[unit_key]["default"] if self.units[unit_key]["default"] is not None else unit
                return final_string
        return str(number)

    def _parse_sentence(self, sentence):
        temp = self.useless_chars_regex.sub("", sentence)
        return [x for x in temp.split() if len(x) > 1]

    def _parse_description(self, description):
        final_numbers = []
        final_words = []
        numbers = self.number_with_regex.findall(description)
        for number in numbers:
            description = description.replace(number, "")
            # try:
            value = self.numbers_regex.search(number).group(0)
            unit = self.all_units_regex_alone.search(number)

            if unit is not None:
                unit = unit.group(2)

                final_string = self.append_unit(value, unit)
                if len(final_string) > 2:
                    final_numbers.append(final_string)
            else:
                final_numbers.append(str(value))
            # except:
            #     print("Could not parse value from description.")
            

            final_words = self._parse_sentence(description)

        return final_words, final_numbers            

    def _remove_frequent(self, products):
        used_key_words = {}
        for product in products:
            for word in product.data["key_words"]:
                if word not in used_key_words.keys():
                    used_key_words[word] = 1
                else:
                    used_key_words[word] += 1
        print(used_key_words)

