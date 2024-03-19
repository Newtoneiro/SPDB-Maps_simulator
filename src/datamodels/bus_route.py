from dataclasses import dataclass


@dataclass
class BusRoute:
    id: int
    name: str
    is_active: bool
    stop_list: list

    def __str__(self):
        return f"[BusRoute] {self.id}: {self.name}"
    
    def __repr__(self):
        return f"{self.id}: {self.name}"
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)