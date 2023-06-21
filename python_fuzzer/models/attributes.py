from typing import List

attributes: List[List[str]] = [
    ["listID", "listAgencyID", "listAgencyName", "listVersionID"], #code -str
    ["schemeID", "schemeAgencyID", "schemeAgencyName"], #identifier ID -str
    ["languageID"], #text, name - str
    ["UnitCode"], #quantity, measure - float
    ["CurrencyID"], #amount -float
    ["mimeCode", "encodingCode", "characterSetCode"] #binary
]