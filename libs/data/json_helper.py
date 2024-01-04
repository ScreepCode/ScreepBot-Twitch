import json

FILENAME = "libs/data/data.json"


def _load_json(filename=FILENAME) -> dict:
    with open(filename, encoding="UTF-8") as json_file:
        data = json.load(json_file)
        return data


def _write_json(json_data, filename=FILENAME) -> None:
    json_string: str = json.dumps(json_data, indent=4, ensure_ascii=False)
    with open(filename, 'w', encoding="UTF-8") as outfile:
        outfile.write(json_string)


def update_json(key, new_data) -> None:
    data: dict = _load_json()
    data[key] = new_data
    _write_json(data)


def get_relevant_information(topic) -> dict:
    data: dict = _load_json()
    return data[topic]
