import pathlib
import time
import json


def write_json(path: str, filename: str, content: str):
    # Create the folders if the path doesn't exist
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    with open(f'{path}/{filename}.json', 'w') as f:
        f.write(content)


def timestamp():
    return round(time.time())
