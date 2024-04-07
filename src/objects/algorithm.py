import heapq
from src.datamodels import Node, Path


class Dijkstra:
    def __init__(self, nodes, paths):
        self.graph = self._generate_graph(nodes, paths)

    def find_shortest_paths(self, start, destinations) -> list[Path]:
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        previous = {node: None for node in self.graph}
        reached_destinations = set()

        while pq and len(reached_destinations) < len(destinations):
            current_distance, current_node = heapq.heappop(pq)
            if current_node in destinations:
                reached_destinations.add(current_node)

            for neighbor, path in self.graph[current_node].items():
                distance = current_distance + path.distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        if len(reached_destinations) == len(destinations):
            paths = []
            for destination in destinations:
                path = []
                current_node = destination
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous[current_node]
                paths[destination] = path[::-1]
            return paths

        return None

    def _generate_graph(nodes, paths):
        graph = {node: {} for node in nodes}
        for path in paths:
            graph[path.from_node][path.to_node] = path
        return graph
