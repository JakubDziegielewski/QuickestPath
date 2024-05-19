import pandas as pd
import geopandas as gpd
import networkx as nx


# metoda pozwalająca na wyznaczenie bbox na podstawie posiadanego grafu G
# ma to na celu późniejsze eliminowanie zapytań spoza obszaru objętego naszą mapą
def calculate_bbox(G: nx.MultiDiGraph) -> (float, float, float, float):
    min_lon = float("inf")
    min_lat = float('inf')
    max_lon = float('-inf')
    max_lat = float('-inf')
    
    for _, data in G.nodes(data=True):
        lon = data.get("y", None)
        lat = data.get("x", None)
        
        if lon is not None and lat is not None:
            if lon < min_lon:
                min_lon = lon
            if lon > max_lon:
                max_lon = lon
            if lat < min_lat:
                min_lat = lat
            if lat > max_lat:
                max_lat = lat
                
    return (min_lon, min_lat, max_lon, max_lat)
    

# metoda ma na celu uzupełnienie wartości "maxspeed", dla którego wiele krawędzi ma brakujące info
# na podstawie atrybutu "highway", który zawsze jest obecny
def fill_max_speed(row: pd.Series) -> int:
    if row["maxspeed"] == "PL:urban":
        return 50
    elif row["maxspeed"] == "30 mph":
        return 30
    elif row["maxspeed"] != None:
        return int(row["maxspeed"])
    elif row["highway"] == "motorway":
        return 140
    elif row["highway"] == "trunk":
        return 120
    elif row["highway"] == "primary":
        return 90
    elif row["highway"] == "secondary":
        return 70
    elif row["highway"] in ["motorway_link", "primary_link", "trunk_link"]:
        return 60
    elif row["highway"] in ["tertiary", "unclassified", "secondary_link"]:
        return 50
    else:
        return 30
    
    
# metoda mająca na celu oczyścić nasz zbiór potencjalnych krawędzi z punktów niebędących drogami
# pozbywamy się również wielu niepotrzebnych w naszym zastosowaniu atrybutów
# ma to na celu przyspieszenie generowania grafu    
def clean_edges_data(edges: gpd.geodataframe.GeoDataFrame):
        
    # wyznaczamy indeksy rzędów, które prawdopodobnie zawierają błędne dane
    index_1 = edges.index[edges["access"].isin(["no", "emergency", "military", "bus", "employees", "forestry"])]
    index_2 = edges.index[edges["area"].isin(["no", "yes"])]
    index_3 = edges.index[edges["bicycle"].isin(["designated", "destination", "dismount", "official", "permit"])]
    index_4 = edges.index[edges["foot"].isin(["designated", "destination", "permit"])]
    index_5 = edges.index[edges["highway"].isin(["bridleway", "cyclist_waiting_aid", "road", "steps", "cycleway", "path"])]
    index_6 = edges.index[edges["motorcar"].isin(["delivery", "destination", "forestry", "agricultural"])]
    index_7 = edges.index[edges["motor_vehicle"].isin(["delivery", "destination", "forestry", "agricultural", "official", "forestry"])]
    index_8 = edges.index[edges["service"].isin(["yard", "*", "da", "spur", "fire_road", "droga_wewnetrzna"])]
    index_9 = edges.index[edges["surface"].isin(["grass", "grass_paver", "rock", "paving_stones:30", "wood", "woodchips"])]
    index_10 = edges.index[edges["tracktype"].isin(["grade1", "grade2", "grade3", "grade4", "grade5"])] 
    
    # łączymy znalezione indeksy w jeden i dokonujemy usunięcia wątpliwej jakości rekordów
    indexes = index_1.union(index_2).union(index_3).union(index_4).union(index_5).union(index_6).union(index_7).union(index_8).union(index_9).union(index_10)
    edges.drop(indexes, inplace=True)
    
    # skorzystawszy z zawartych w danych kolumnach informacji, możemy się ich pozbyć
    edges.drop(columns=["access", "area", "bicycle", "busway", "cycleway", "est_width",
                        "foot", "footway", "int_ref", "lit", "motorcar", "motorroad",
                        "motor_vehicle", "overtaking", "passing_places", "psv", "service",
                        "segregated", "sidewalk", "smoothness", "surface", "tracktype", "turn",
                        "width", "timestamp", "version", "osm_type"], inplace=True)