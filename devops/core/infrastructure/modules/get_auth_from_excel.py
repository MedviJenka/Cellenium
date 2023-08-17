import csv


def _read_csv(path: str) -> dict[str]:

    desired_columns = ["Access key ID",	"Secret access key"]

    with open(path, newline='') as csvfile:

        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        second_row = next(csv_reader)
        extracted_data = {column_name: second_row[index] for index, column_name in enumerate(desired_columns)}

    return extracted_data


def get_access_key(path: str) -> str:
    return _read_csv(path)["Access key ID"]


def get_secret_key(path: str) -> str:
    return _read_csv(path)["Secret access key"]
