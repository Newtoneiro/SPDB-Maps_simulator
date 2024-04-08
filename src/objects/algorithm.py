import heapq
from typing import Dict, List
from src.datamodels import Node, Path

class Dijkstra:
    def __init__(self, nodes: List[Node], paths: List[Path]):
        self.graph = self._generate_graph(nodes, paths)

    def find_shortest_paths(self, start: Node, destinations: List[Node]) -> Dict[Node, Path]:
        # Initialize distances to all nodes as infinity
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0  # Distance from start node to itself is 0

        # Priority queue for nodes to visit next
        priority_queue = [(0, start)]  # (distance, node)

        # Previous node in the shortest path
        previous = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If destination is reached, stop exploration
            if current_node in destinations:
                break

            # Explore neighbors of the current node
            for neighbor, edge in self.graph[current_node].items():
                distance = current_distance + edge.distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    previous[neighbor] = current_node

        # Reconstruct shortest paths to destinations
        shortest_paths = {}
        for destination in destinations:
            path = []
            node = destination
            while node is not None:
                path.insert(0, node)
                node = previous[node]
            shortest_paths[destination] = path

        return shortest_paths

    def _generate_graph(self, nodes: List[Node], paths: List[Path]) -> Dict[Node, Dict[Node, Path]]:
        graph = {node: {} for node in nodes}
        for path in paths:
            graph[path.from_node][path.to_node] = path
        return graph