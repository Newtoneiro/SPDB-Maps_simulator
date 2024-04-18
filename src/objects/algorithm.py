import heapq
from src.datamodels import Node, Path
from src.constants import ALOGRITHM_CONSTANTS


class Dijkstra:
    def __init__(self, nodes: list[Node], paths: list[Path]):
        self.graph = self._generate_graph(nodes, paths)

    def find_shortest_paths(
        self, selected_nodes: list[Node], cost_type, left_turn_mode
    ) -> list[Node]:
        """
        Finds the shortest path between selected nodes based on given cost.
        :param selected_nodes: list of selected nodes.
        :return: list of nodes in the shortest path.
        """
        if len(selected_nodes) < 2:
            return []

        for idx in range(len(selected_nodes) - 1):
            start = selected_nodes[idx]
            destination = selected_nodes[idx + 1]
            path = self._find_shortest_path(
                start, destination, cost_type, left_turn_mode
            )
            if idx == 0:
                shortest_path = path
            else:
                shortest_path.extend(path[1:])

        return shortest_path

    def _find_shortest_path(
        self, start: Node, destination: Node, cost_type, left_turn_mode
    ) -> list[Node]:
        """
        Finds the shortest path between two nodes based on given cost.
        :param start: start node.
        :param destination: destination node.
        :param cost_type: cost type.
        :param left_turn_mode: left turn mode.
        :return: list of nodes in the shortest path.
        """
        # Initialize distances to all nodes as infinity
        costs = {node: float("inf") for node in self.graph}
        costs[start] = 0  # Distance from start node to itself is 0

        # Priority queue for nodes to visit next
        priority_queue = [(0, start)]  # (distance, node)

        # Previous node in the shortest path
        previous = {node: None for node in self.graph}

        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)

            # If destination is reached, stop exploration
            if current_node == destination:
                break

            # Explore neighbors of the current node
            for neighbor, path in self.graph[current_node].items():
                # Adjust distance considering left turn
                if (
                    left_turn_mode == True
                    and current_node != start
                    and self.is_left_turn(
                        previous[current_node], current_node, neighbor
                    )
                ):
                    if cost_type == ALOGRITHM_CONSTANTS.DISTANCE_MODE:
                        cost = (
                            current_cost
                            + path.distance
                            + ALOGRITHM_CONSTANTS.LEFT_TURN_DISTANCE_PENALTY
                        )
                    elif cost_type == ALOGRITHM_CONSTANTS.TIME_MODE:
                        cost = (
                            current_cost
                            + path.travel_time
                            + ALOGRITHM_CONSTANTS.LEFT_TURN_DISTANCE_PENALTY
                        )
                else:
                    if cost_type == ALOGRITHM_CONSTANTS.DISTANCE_MODE:
                        cost = current_cost + path.distance
                    elif cost_type == ALOGRITHM_CONSTANTS.TIME_MODE:
                        cost = current_cost + path.travel_time

                if cost < costs[neighbor]:
                    costs[neighbor] = cost
                    heapq.heappush(priority_queue, (cost, neighbor))
                    previous[neighbor] = current_node

        # Reconstruct shortest path to destination
        path = []
        node = destination
        while node is not None:
            path.insert(0, node)
            node = previous[node]

        return path

    def is_left_turn(
        self, previous_node: Node, current_node: Node, next_node: Node
    ) -> bool:
        """
        Checks if the turn from the current node to the next node is a left turn.
        """
        # Determine the vectors representing the current and next segments
        current_vector = (
            previous_node.coordinates.x - next_node.coordinates.x,
            previous_node.coordinates.y - next_node.coordinates.y,
        )
        next_vector = (
            current_node.coordinates.x - previous_node.coordinates.x,
            current_node.coordinates.y - previous_node.coordinates.y,
        )

        # Calculate the cross product of the vectors
        cross_product = (
            current_vector[0] * next_vector[1] - current_vector[1] * next_vector[0]
        )

        # If the cross product is negative, it's a left turn (because we are using a coordinate system where the y-axis is inverted)
        return cross_product < 0

    def _generate_graph(
        self, nodes: list[Node], paths: list[Path]
    ) -> dict[Node, dict[Node, Path]]:
        graph = {node: {} for node in nodes}
        for path in paths:
            graph[path.from_node][path.to_node] = path
        return graph
