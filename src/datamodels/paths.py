"""
This module contains the Stop data model.
"""

from dataclasses import dataclass
from src.datamodels.nodes import Node


@dataclass
class Path:
    id: int
    from_node: Node
    to_node: Node
    distance: float
    travel_time: float

    def __str__(self):
        return f"[Path] {self.id}: {self.from_node.coordinates} -> {self.to_node.coordinates} ({self.distance} m, {self.travel_time} s)"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
