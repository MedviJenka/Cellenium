import json


def read_json(path: str) -> dict:
    output = json.load(open(path))
    return {
        'original': output['original'],
        'actual': output['actual'],
        'percentage_threshold': output['percentage_threshold'],
        'resolution': output['resolution']
    }
