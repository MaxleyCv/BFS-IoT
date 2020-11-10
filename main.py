import doctest
from graph import *

INPUT_FILE = open("career.in", "r")
OUTPUT_FILE = open("career.out", "w")


def get_maximum_profit(hierarchy):
    """
    The function to implement a search for maximum value path
    :param hierarchy: graph of pyramidal type
    :return: maximum path weight
    >>> get_maximum_profit(get_items())
    13
    >>> G = Graph()
    >>> G.add_vertex(4, [])
    >>> G.add_vertex(1, [])
    >>> G.add_vertex(2, [0, 1])
    >>> get_maximum_profit(G)
    6
    """
    if len(hierarchy.vertexes):
        hierarchy.breadth_search([len(hierarchy.vertexes) - 1], is_first=True)
        return hierarchy.max_profit
    else:
        return 0


def generate_indexes(level_length, index, graph_length):
    """
    A function to generate connections between the vertexes in a pyramidal type
    :param level_length: the length of the level of the graph
    :param index: the index of a vertex in level
    :param graph_length: maximum index of a vertex before the level was added
    :return: maximum path weight
    >>> generate_indexes(4, 2, 11)
    [9, 8]
    >>> generate_indexes(5, 1, 6)
    [2, 1]
    >>> generate_indexes(2, 1, 7)
    [6, 5]
    """
    if index >= level_length:
        raise ValueError

    new_id = graph_length + index
    return [(new_id - level_length), new_id - level_length - 1]


def get_items():
    """
    A function to read graph from a file
    :return: Graph of the type as in the task read from input file
    """
    hierarchy = Graph()
    income = INPUT_FILE.readlines()
    for i in range(len(income)):
        income[i] = str.replace(income[i], '\n', '')

    if not len(income):
        return hierarchy

    length = int(income.pop(0))

    for level in range(length):
        new_level = list(map(int, income.pop().split(' ')))
        prev_length = len(hierarchy.vertexes)

        for new_index in range(len(new_level)):
            if len(new_level) == length:
                hierarchy.add_vertex(new_level[new_index], [])
            else:
                hierarchy.add_vertex(new_level[new_index], generate_indexes(len(new_level), new_index, prev_length))
            
    return hierarchy


if __name__ == "__main__":
#    doctest.testmod(verbose=True)
    OUTPUT_FILE.write(str(get_maximum_profit(get_items())))

