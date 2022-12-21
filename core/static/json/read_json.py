import json
from dataclasses import dataclass





@dataclass
class ReadJson:

    path: str = r'C:\Users\evgenyp\Cellenium\core\static\json\data.json'

    def read_json(self) -> dict:
        output = json.load(open(self.path))

        return output

    def __getitem__(self, index: str) -> str:
        return self.read_json()[index]



if __name__ == "__main__":
    read = ReadJson()
    read.read_json['actual']

        #
        # return {
        #     'original': output['original'],
        #     'actual': output['actual'],
        #     'percentage_threshold': output['percentage_threshold'],
        #     'resolution': output['resolution']
        # }
