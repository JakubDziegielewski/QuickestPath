import osmnx as ox
import networkx as nx


# klasa ma na celu umożliwienie usługi geomapowania
# otrzymując adres w formie tekstowej znajduje dla niego najbliższy możliwy węzeł w grafie
class GeoMapper:
    
    def map(self, G: nx.MultiDiGraph, address: str) -> int:
        y, x = ox.geocode(address) # throws InsufficientResponseError
        return ox.distance.nearest_nodes(G, x, y)
    