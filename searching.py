import os

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
    #csw_path = Path.cwd()
    import json
    json_filename = 'sequential.json'
    json_data = {"unordered_numbers", "ordered_numbers", "dna_sequence"}
    with open(json_filename, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)
        if field not in data:
            return None

        return data[field]
        json.dump(json_data, file_obj)

def linear_search(sequence, target):
    positions = []
    count = 0

    for index, value in enumerate(sequence):
        if value == target:
            positions.append(index)
            count += 1

    return {
        "positions": positions,
        "count": count
    }

def main():
        sequential_data = read_data("sequential.json", "unordered_numbers")
        print(sequential_data)

def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")

    if sequential_data is None:
        print("Chyba při načítání dat.")
        return


    target_number = 5


    result = linear_search(sequential_data, target_number)

    print("Data:", sequential_data)
    print(f"Hledané číslo: {target_number}")
    print("Výsledek:", result)



if __name__ == '__main__':
    main()