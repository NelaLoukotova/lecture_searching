from random import choices


def unordered_sequence(max_len=100):
    """
    Returns list of unordered ints from within a range between -1000 and 1000.
    :param max_len: (int) desired length of sequence
    :return: (list) sequence of numbers
    """
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    """
    Returns list of ordered ints from within a range between -1000 and 1000.
    :param max_len: (int) desired length of sequence
    :return: (list) sequence of numbers
    """
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    """
    Returns string of randomly generated DNA sequence.
    :param max_len: (int) desired length of sequence
    :return: (str) sequence of basis T, G, A, C
    """
    return ''.join(choices('TGAC', k=max_len))

def generate_test_sizes():
    """
    Returns list of sizes for testing.
    """
    return [100, 500, 1000, 5000, 10000]


def generate_ordered_sequences(sizes):
    """
    Returns dictionary: size -> ordered sequence
    """
    return {size: ordered_sequence(size) for size in sizes}


def generate_unordered_sequences(sizes):
    """
    Returns dictionary: size -> unordered sequence
    """
    return {size: unordered_sequence(size) for size in sizes}


def main():
    """
    Test function
    :return:
    """
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()

