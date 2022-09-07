from typing import List


def convert_main_db_response(json: dict) -> List[dict]:
    tables: List[dict] = json['r']['tables']
    data: List[dict] = list()

    for table in tables:
        df = parse_json_to_dictionary(table)
        data.append(df)

    return data


def parse_json_to_dictionary(data: dict) -> dict:
    data_rows: List[dict] = data['data_rows']
    dataset: dict = dict()

    for row in data_rows:
        if len(row) == 2:
            id, value = row.values()
            dataset[id] = value
        elif len(row) == 4:
            id, _, starttime, endtime = row.values()
            dataset[id] = (starttime, endtime)
        else:
            raise ValueError(f'{row=}')

    return dataset
