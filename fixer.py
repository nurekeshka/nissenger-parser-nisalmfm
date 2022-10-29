from typing import Dict


class BaseFixer(object):
    dictionary: Dict[str, str] = None

    def __init__(self):
        pass
    
    def fix(self, string: str) -> str:
        if string in self.dictionary.keys():
            return self.dictionary[string]

    def format(self, string: str) -> str:
        return string.lower().title()

