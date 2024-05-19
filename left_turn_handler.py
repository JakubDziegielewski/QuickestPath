import networkx as nx
from graph_utils import get_vector_between_nodes, calculate_sin, calculate_cos, calculate_angle


# klasa ma na celu udostępnienie funkcjonalności rozpoznawania skrętów w lewo w grafie
# dla podanych trzech węzłów, główna metoda zwraca info, czy skręt między nimi jest w lewo, czy nie
# dla rozpoznanego skrętu w lewo umożliwia również obliczenie kary na podstawie param wejściowych
class LeftTurnHandler:
            
    def __init__(self, penalty_to_better_road: float, penalty_to_equal_road: float, penalty_to_worse_road: float, min_angle_left_turn: float):
        self._penalty_to_better_road = penalty_to_better_road
        self._penalty_to_equal_road = penalty_to_equal_road
        self._penalty_to_worse_road = penalty_to_worse_road
        self._min_angle_left_turn = min_angle_left_turn


    def is_turn_left(self, G: nx.MultiDiGraph, first_node_id: int, second_node_id: int, third_node_id: int) -> bool:
        
        # jeżeli środkowy węzeł ma tylko 2 wychodzące krawędzie to wiadomo, że jest to węzeł w środku drogi
        if len(G[second_node_id]) == 2:
            return False
        
        # wyznacz wektory pomiędzy punktami 
        vector_a = get_vector_between_nodes(G, first_node_id, second_node_id)
        vector_b = get_vector_between_nodes(G, second_node_id, third_node_id)        
        
        # wyznacz sin i cos powyższych wektorów
        sin_alpha = calculate_sin(vector_a, vector_b)
        cos_alpha = calculate_cos(vector_a, vector_b)
        
        # wyznacz kąt (w stopniach)
        alpha = calculate_angle(sin_alpha, cos_alpha)

        # jeśli obliczony kąt jest większy niż zadana wartość klasyfikująca skręt jako skręt w lewo
        # to zwracamy True, wpp: False
        if alpha > self._min_angle_left_turn:
            return True
        return False
        
    
    def calculate_penalty(self, G: nx.MultiDiGraph, first_node_id: int, second_node_id: int, third_node_id: int) -> float:
        pass
