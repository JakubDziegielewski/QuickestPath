import networkx as nx
from graph_utils import calculate_euclid_dist
from a_star import BestPathFinder

# ta klasa ma na celu zwrócenie rozwiązania problemu wyszukiwania najlepszej
# ścieżki pomiędzy wieloma zadanymi punktami
# wykorzystywany będzie algorytm aproksymacyjny Nearest Neighbor 
# oznacza to, że z danego punktu wyznaczona zostanie ścieżka do najbliższego nieprzetworzonego sąsiada
class TravelSalesmanSolver:
    
    def __init__(self, best_path_finder: BestPathFinder):
        self._best_path_finder = best_path_finder
    
    
    def solve(self, G: nx.MultiDiGraph, nodes: list) -> list:
        
        # zainicjalizuj pusty wynik
        result = []
        
        # wybierz pierwszy węzeł jako punkt startowy
        current_node = nodes[0]
        
        # przechowuj informacje o już przetworzonych węzłach
        visited_nodes = {current_node}
        
        # dopóki wszystkie węzły nie zostaną przetwrzone
        while len(visited_nodes) < len(nodes):
            
            # znajdź najbliższego sąsiada
            nearest_neighbor = self._get_nearest_unvisited_neighbor(G, current_node, nodes, visited_nodes)
            
            # jeśli nie ma sąsiadów do przetworzenia, wyjdź z pętli
            if nearest_neighbor == -1:
                break
            
            # znajdź najlepszą ścieżkę między obecnym węzłem a najbliższym sąsiadem
            # dodaj ją do wyniku
            best_path = self._best_path_finder.find_shortest_path(G, current_node, nearest_neighbor)
            if current_node == nodes[0]:
                result.append(best_path)
            else:
                result.append(best_path[1:])
            
            # powtórz powyższe kroki dla sąsiada
            current_node = nearest_neighbor
            visited_nodes.add(nearest_neighbor)
        
        # złącz wyniki
        combined_result = []
        for subresult in result:
            combined_result.extend(subresult)
        
        # zwróć złączony wynik
        return combined_result
        
    
    def _get_nearest_unvisited_neighbor(self, G: nx.MultiDiGraph, current_node: int, all_nodes: list, visited_nodes: set) -> int:
        
        # zainicjalizuj brak sąsiada i nieskończoną odległość
        nearest_neighbor = -1
        dist_to_nearest_neighbor = float('inf')
        
        # dla każdego sąsiada obecnego węzła
        for neighbor in all_nodes:
            
            # sprawdź, czy nie był on już rozpatrywany
            if neighbor in visited_nodes:
                continue
            
            # oblicz dystans euklidesowy od węzła do sąsiada
            dist = calculate_euclid_dist(G, current_node, neighbor)
            
            # jeśli lepszy niż dotychczas najlepszy znaleziony, uaktualnij info o najlepszym sąsiedzie
            if dist < dist_to_nearest_neighbor:
                nearest_neighbor = neighbor
                dist_to_nearest_neighbor = dist
        
        # zwróć najlepszego znalezionego sąsiada
        return nearest_neighbor
    