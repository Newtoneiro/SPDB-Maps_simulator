"""
This module contains the Stop data model.
"""
from src.datamodels.coordinates import Coordinates
from dataclasses import dataclass


@dataclass
class Landmark:
    id: int
    name: str
    coordinates: Coordinates

    def __str__(self):
        return f"[Stop] {self.id}: {self.name} ({self.coordinates})"

    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)