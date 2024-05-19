import networkx as nx


# klasa ma na celu umożliwić znajdowanie najszybszej ścieżki przejazdu między dwoma (!) węzłami w grafie
# wykorzystywany jest algorytm A* z ustaloną wcześniej heurystyką
# zakładającą maksymalny dopuszczlny maxspeed od następnego węzła w linii prostej do celu
class BestPathFinder:
    
    
    def find_shortest_path(self, G: nx.MultiDiGraph, source: int, dest: int):
        
        
    