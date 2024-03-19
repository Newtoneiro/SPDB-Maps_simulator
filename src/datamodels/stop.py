"""
This module contains the Stop data model.
"""

from dataclasses import dataclass


@dataclass
class Stop:
    id: int
    name: str
    is_active: bool
    coordinates: tuple

    def __str__(self):
        return f"[Stop] {self.id}: {self.name}"
    
    def __repr__(self):
        return f"{self.id}: {self.name}"
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)