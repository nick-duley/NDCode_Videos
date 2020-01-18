from collections import deque, namedtuple

# Every node will have a distance of infinity at first, since we don't know the initial distance
inf = float('inf')

# An edge in the graph will have a distance of infinity at first
Edge = namedtuple('Edge', 'start, end, weight')

# Creates the edge. Defines the start node, end node and the edge's weight


def make_edge(start, end, weight=1):
    return Edge(start, end, weight)


class Graph:
    # Creates the Graph class
    def __init__(self, edges):
        # Ensure data entered into the graph is valid
        wrong_edges = [edge for edge in edges if len(edge) not in [2, 3]]

        if wrong_edges:
            raise ValueError("There's an incorrect number of edges")

        # Store every edge as list
        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def total_nodes(self):
        # Returns a set of the total number of nodes as a set
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    @property
    def neighbours(self):
        # Returns the neighbour nodes for a node as a dictionary
        neighbours = {node: set() for node in self.total_nodes}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.weight))

        return neighbours

    def dijkstra_algorithm(self, source, destination):
        # The initial weight for every node is infinity at first
        weights = {node: inf for node in self.total_nodes}

        # The weight for the source node will be set to 0
        weights[source] = 0
        # Copies the total_nodes set
        nodes = self.total_nodes.copy()

        # Ensure no node has been previously visited
        previous_nodes = {
            node: None for node in self.total_nodes
        }

        while nodes:
            # For every node, get its edge weight
            current_node = min(
                nodes, key=lambda node: weights[node])
            # Ensure no nodes have a distance of infinity
            nodes.remove(current_node)
            if weights[current_node] == inf:
                break
            # If a shorter route between two nodes has been discovered, use that route instead
            for neighbour, weight in self.neighbours[current_node]:
                alternative_route = weights[current_node] + weight
                if alternative_route < weights[neighbour]:
                    weights[neighbour] = alternative_route
                    previous_nodes[neighbour] = current_node

        # Store every visited node as a dequeue object
        path, current_node = deque(), destination

        # Append the node to the dequeue object
        while previous_nodes[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.appendleft(current_node)
        # Return the dequeue object
        return path


# Instantiate the graph object
graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("d", "f", 9)])


display_graph = graph.dijkstra_algorithm("a", "f")
while 0 < len(display_graph):
    node = display_graph.popleft()
    print(node, end="\n")
