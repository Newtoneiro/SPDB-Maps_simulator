import heapq
from src.datamodels import Node, Path


class Dijkstra:
    def __init__(self, nodes: list[Node], paths: list[Path]):
        self.graph = self._generate_graph(nodes, paths)

    def find_shortest_paths_distance(self, selected_nodes: list[Node]) -> list[Node]:
        """
        Finds the shortest path between selected nodes based on distance.
        :param selected_nodes: list of selected nodes.
        :return: list of nodes in the shortest path.
        """
        if len(selected_nodes) < 2:
            return []

        for idx in range(len(selected_nodes) - 1):
            start = selected_nodes[idx]
            destination = selected_nodes[idx + 1]
            path = self.find_shortest_path_distance(start, destination)
            if idx == 0:
                shortest_path = path
            else:
                shortest_path.extend(path[1:])

        return shortest_path

    def find_shortest_path_distance(self, start: Node, destination: Node) -> list[Node]:
        """
        Finds the shortest path between two nodes.
        """
        # Initialize distances to all nodes as infinity
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0  # Distance from start node to itself is 0

        # Priority queue for nodes to visit next
        priority_queue = [(0, start)]  # (distance, node)

        # Previous node in the shortest path
        previous = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If destination is reached, stop exploration
            if current_node == destination:
                break

            # Explore neighbors of the current node
            for neighbor, path in self.graph[current_node].items():
                distance = current_distance + path.distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    previous[neighbor] = current_node

        # Reconstruct shortest path to destination
        path = []
        node = destination
        while node is not None:
            path.insert(0, node)
            node = previous[node]

        return path

    def find_shortest_paths_time(self, selected_nodes: list[Node]) -> list[Node]:
        """
        Finds the shortest path between selected nodes based on time.
        :param selected_nodes: list of selected nodes.
        :return: list of nodes in the shortest path.
        """
        if len(selected_nodes) < 2:
            return []

        for idx in range(len(selected_nodes) - 1):
            start = selected_nodes[idx]
            destination = selected_nodes[idx + 1]
            path = self.find_shortest_path_time(start, destination)
            if idx == 0:
                shortest_path = path
            else:
                shortest_path.extend(path[1:])

        return shortest_path

    def find_shortest_path_time(self, start: Node, destination: Node) -> list[Node]:
        # Initialize times to all nodes as infinity
        times = {node: float("inf") for node in self.graph}
        times[start] = 0  # time from start node to itself is 0

        # Priority queue for nodes to visit next
        priority_queue = [(0, start)]  # (time, node)

        # Previous node in the shortest path
        previous = {node: None for node in self.graph}

        while priority_queue:
            current_time, current_node = heapq.heappop(priority_queue)

            # If destination is reached, stop exploration
            if current_node == destination:
                break

            # Explore neighbors of the current node
            for neighbor, path in self.graph[current_node].items():
                time = current_time + path.travel_time
                if time < times[neighbor]:
                    times[neighbor] = time
                    heapq.heappush(priority_queue, (time, neighbor))
                    previous[neighbor] = current_node

        # Reconstruct shortest path to destination
        path = []
        node = destination
        while node is not None:
            path.insert(0, node)
            node = previous[node]

        return path

    def _generate_graph(
        self, nodes: list[Node], paths: list[Path]
    ) -> dict[Node, dict[Node, Path]]:
        graph = {node: {} for node in nodes}
        for path in paths:
            graph[path.from_node][path.to_node] = path
        return graph
