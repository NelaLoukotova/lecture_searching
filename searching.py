import os
from generators import ordered_sequence
import time
import random
import matplotlib.pyplot as plt
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
def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

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

def main():

    unordered_data = read_data("sequential.json", "unordered_numbers")
    target_number = 5

    if unordered_data:
        linear_result = linear_search(unordered_data, target_number)
        print("Linear search:", linear_result)


    ordered_data = read_data("sequential.json", "ordered_numbers")

    if ordered_data is None:
        print("Chyba při načítání seřazených dat.")
        return

    binary_result = binary_search(ordered_data, target_number)

    print("Seřazená data:", ordered_data)
    print(f"Hledané číslo: {target_number}")
    print("Binary search index:", binary_result)


def main():
    sizes = [100, 500, 1000, 5000, 10000]

    linear_times = []
    binary_times = []
    set_times = []

    repeats = 50

    for size in sizes:
        arr = ordered_sequence(size)
        s = set(arr)

        lin_total = 0
        bin_total = 0
        set_total = 0

        for _ in range(repeats):
            target = random.choice(arr)


            start = time.perf_counter()
            linear_search(arr, target)
            lin_total += time.perf_counter() - start


            start = time.perf_counter()
            binary_search(arr, target)
            bin_total += time.perf_counter() - start


            start = time.perf_counter()
            target in s
            set_total += time.perf_counter() - start

        linear_times.append(lin_total / repeats)
        binary_times.append(bin_total / repeats)
        set_times.append(set_total / repeats)


    plt.figure(figsize=(10, 6))

    plt.plot(sizes, linear_times, label="Lineární vyhledávání")
    plt.plot(sizes, binary_times, label="Binární vyhledávání")
    plt.plot(sizes, set_times, label="Set (množina)")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas (s)")
    plt.title("Porovnání vyhledávacích algoritmů")

    plt.legend()
    plt.grid()

    plt.show()


if __name__ == '__main__':
    main()