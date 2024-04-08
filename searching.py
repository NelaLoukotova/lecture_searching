import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_name} does not exist.")
        return None

    # Check if the file is a json file
    if not file_name.endswith('.json'):
        print(f"File {file_name} is not a JSON file.")
        return None

    # Check if the field is valid
    with open("sequential.json", 'r') as f:
        allowed_fields = json.load(f).keys()

    if field not in allowed_fields:
        print(f"Field {field} is not allowed.")
        return None

    # Read the json file and return the specified field
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data[field]


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)


if __name__ == '__main__':
    main()
1