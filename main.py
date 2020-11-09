import copy
import doctest

INPUT_FILE = open("career.in", "r")
OUTPUT_FILE = open("career.out", "w")


class Vertex:
    """
    Vertex of the graph, has connections that are relative for a particular graph
    (e.g. one vertex is impossible to use in two different graphs)
    """

    def __init__(self, val):
        self.value = val
        self.connections = []
        self.pathway = 0


class Graph:
    """
    Class for iplementation of the graphs
    Has a list of Vertexes, each vertex has value and maximum pathway property
    """

    def __init__(self):
        self.vertexes = []
        self.max_profit = 0

    def add_vertex(self, val, connections):
        new_vertex = Vertex(val)
        new_vertex.connections = copy.deepcopy(connections)
        self.vertexes.append(new_vertex)

    def breadth_search(self, indexes, is_first=False):
        """
        Breadth search part of algorithm, generates next vertexes to search from
        The search chooses maximum weight path
        Result of maximum weight path is stored in the graph
        :param indexes: indexes of the graph
        :return: nothing
        >>> G = Graph()
        >>> G.add_vertex(4, [])
        >>> G.add_vertex(1, [])
        >>> G.add_vertex(2, [0, 1])
        >>> G.add_vertex(3, [2])
        >>> G.breadth_search([3], is_first=True)
        >>> G.max_profit
        9
        """
        if is_first:
            self.vertexes[indexes[0]].pathway = self.vertexes[indexes[0]].value
        next_indexes = []
        for index in indexes:
            current = copy.deepcopy(self.vertexes[index])
            if current.pathway > self.max_profit:
                self.max_profit = current.pathway
            if len(current.connections):
                for new_index in self.vertexes[index].connections:
                    next_vertex = copy.deepcopy(self.vertexes[new_index])
                    if next_vertex.pathway <= current.pathway + next_vertex.value:
                        self.vertexes[new_index].pathway = current.pathway + next_vertex.value
                        next_indexes.append(new_index)
                    else:
                        continue
        if len(next_indexes):
            self.breadth_search(next_indexes)
        else:
            return


def get_maximum_profit(hierarchy):
    """
    :param hierarchy: biased self of pyramydial hierarchy
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
    new_id = graph_length + index
    return [(new_id - level_length), new_id - level_length - 1]


def get_items():
    """
    A function to read from a file
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

