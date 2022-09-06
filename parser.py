from typing import List


def convert_main_db_response(json: dict) -> List[dict]:
    tables: List[dict] = json['r']['tables']
    data: list = list()

    for table in tables:
        df = parse_json_to_dictionary(table)
        data.append(df)

    return data


def parse_json_to_dictionary(data: dict) -> dict:
    data_rows: List[dict] = data['data_rows']
    dataset: dict = dict()

    for row in data_rows:
        try:
            id, value = row.values()
        except ValueError:
            values = tuple(row.values())
            id = values[0]
            value = values[1 : ]

        dataset[id] = value

    return dataset
