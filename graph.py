import copy


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
        """
        Method adds new vertex to a graph, and adds connections to other vertexes
        :param val: value of new vertex
        :param connections: list of connections
        :return: nothing
        """
        new_vertex = Vertex(val)
        new_vertex.connections = copy.deepcopy(connections)
        for vertex in self.vertexes:
            vertex.pathway = 0
        self.vertexes.append(new_vertex)

    def breadth_search(self, indexes, is_first=False):
        """
        Breadth search part of algorithm, generates next vertexes to search from
        The search chooses maximum weight path
        Result of maximum weight path is stored in the graph
        :param indexes: indexes of the graph
        :param is_first: True when the breadth first search starts with the vertexes
        :return: nothing
        >>> G = Graph()
        >>> G.add_vertex(4, [])
        >>> G.add_vertex(1, [])
        >>> G.add_vertex(2, [0, 1])
        >>> G.add_vertex(3, [2])
        >>> G.breadth_search([3], is_first=True)
        >>> G.max_profit
        9
        >>> G.add_vertex(4, [])
        >>> G.vertexes[3].pathway
        0
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
