import re
from extract_words import _extract_words


class Preprocessor():
    def __init__(self):

        self.units = {
            "length": {
                "pattern": r"km|m|cm|dm|mm|\"|inch|inches",
                "default": "mm",
                "conversions": {
                    "km": 1000000,
                    "m": 1000,
                    "dm": 100,
                    "cm": 10,
                    "mm": 1,
                    "inch": 25.4,
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
        self.all_units_pattern.strip("|")

        self.all_units_regex = re.compile(
            r"([\(\[\{]|\s|^)(" + self.all_units_pattern + r")(\s|$|[\)\]\}])", re.IGNORECASE)
        self.numbers_regex = re.compile(r"\d+[\,\.]?[\d]+", re.IGNORECASE)

        self.useless_chars_regex = re.compile(r"[\(\){}\[\]]")

    def preprocess_data(self, products):
        for product in products:
            self._extract_key_features(product)
            product.data["key_name"] = product.data["name"].split()
        pass

    def _extract_key_features(self, product):
        product.data["key_numbers"] = set()
        product.data["key_words"] = set()

        if "additionalproperty" not in product.data.keys():
            return

        for ad in product.data["additionalproperty"]:
            found_number = self._parse_value(ad)
            if found_number is not None:
                for num in found_number:
                    product.data["key_numbers"].add(num.lower().strip())
            else:
                for word in self._parse_word(ad):
                    product.data["key_words"].add(word)

    def _parse_value(self, property):
        unit = None
        numbers = self.numbers_regex.findall(property["value"])
        if len(numbers) != 0:
            numbers = [number.replace(",", ".") for number in numbers]
            unit_match = self.all_units_regex.search(
                property["value"], re.IGNORECASE)
            if unit_match is not None:
                if len(self.all_units_regex.findall(property["value"], re.IGNORECASE)) > 1:
                    return None
            else:
                unit_match = self.all_units_regex.search(
                    property["value"], re.IGNORECASE)
            if unit_match is None:
                return [str(round(float(num))) for num in numbers]

            # Unit found
            unit = unit_match.group(2)
            for unit_key in self.units:
                if unit in self.units[unit_key]["pattern"].split("|"):
                    # try:
                    numbers = [str(round(float(
                        number) * self.units[unit_key]["conversions"][unit])) for number in numbers]
                    return [number + (self.units[unit_key]["default"] if self.units[unit_key]["default"] is not None else unit) for number in numbers]
                    # except:
                    #     print("Error converting property number.")
                    #     return None

        else:  # number not found
            return None

    def _parse_word(self, property):
        temp = self.useless_chars_regex.sub("", property["value"])
        return [x for x in temp.split() if len(x) > 1] 
