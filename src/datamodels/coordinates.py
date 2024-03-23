"""
This module contains the Stop data model.
"""

from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: str

    def __str__(self):
        return f"[Coordinates] ({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))