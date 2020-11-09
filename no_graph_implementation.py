import doctest

INPUT_FILE = open("career.in", "r")
OUTPUT_FILE = open("career.out", "w")


def get_input():
    """
    Function to get list of lists of vertexes
    :return: list of levels
    """
    result = []
    income = INPUT_FILE.readlines()
    for i in range(len(income)):
        income[i] = str.replace(income[i], '\n', '')
    length = int(income.pop(0))
    for i in range(length):
        result.append(list(map(int, income[i].split(' '))))
    return result


def get_max_career(items):
    """
    Main function to find maximum
    :param items: list of levels in company
    :return: maximum career growth
    >>> get_max_career([[1], [2, 3], [1, 9, 2]])
    13
    >>> get_max_career([[0], [1, 1], [2, 3, 2], [10, 11, 9, 8]])
    15
    """
    indexes = range(1, len(items))
    indexes = reversed(indexes)
    for i in indexes:
        for new_index in range(len(items[i]) - 1):
            items[i - 1][new_index] += max(items[i][new_index], items[i][new_index + 1])
    return items[0][0]


if __name__ == "__main__":
#    doctest.testmod(verbose=True)
    OUTPUT_FILE.write(str(get_max_career(get_input())))
