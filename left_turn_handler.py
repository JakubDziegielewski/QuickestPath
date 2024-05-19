import networkx as nx

# klasa ma na celu udostępnienie funkcjonalności rozpoznawania skrętów w lewo w grafie
# dla podanych trzech węzłów, główna metoda zwraca info, czy skręt między nimi jest w lewo, czy nie
# dla rozpoznanego skrętu w lewo umożliwia również obliczenie kary na podstawie param wejściowych
class LeftTurnHandler:
            
    def __init__(self, penalty_to_better_road: float, penalty_to_equal_road: float, penalty_to_worse_road: float):
        self._penalty_to_better_road = penalty_to_better_road
        self._penalty_to_equal_road = penalty_to_equal_road
        self._penalty_to_worse_road = penalty_to_worse_road


    def is_turn_left(self, G: nx.MultiDiGraph, first_node_id: int, second_node_id: int, third_node_id: int) -> bool:
        pass
    
    
    def calculate_penalty(self, G: nx.MultiDiGraph, first_node_id: int, second_node_id: int, third_node_id: int) -> float:
        pass