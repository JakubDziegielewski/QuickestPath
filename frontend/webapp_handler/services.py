import requests
from xml.etree import ElementTree as ET
import json
from src.app import App

def find_feature(array, low, high, id):
    if high >= low:
        mid = low + (high - low) // 2
    if array[mid]['id'] == id:
        return mid
    elif int(array[mid]['id']) > int(id):
            return find_feature(array, low, mid - 1, id)
    else:
        return find_feature(array, mid + 1, high, id)
def process_text_list(text_list, app: App):
    # Example processing: convert all texts to uppercase
    processed_list = [text for text in text_list]
    list_of_nodes = app.run_query(processed_list)
    string_nodes = [str(x) for x in list_of_nodes]
    result = ", ".join(string_nodes).replace('\n', '')
    data = "(node(id:" + result + "););out body;".replace("\n", "")
    r = requests.post("https://overpass-api.de/api/interpreter", data=data)
    root =  ET.fromstring(r.text)
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for node in root.findall('node'):
        feature = {
            "type": "Feature",
            "id": node.get('id'),
            "geometry": {
                "type": "Point",
                "coordinates": [float(node.get('lon')), float(node.get('lat'))]
            }
        }
        geojson["features"].append(feature)
    geojson_result = {
        "type": "FeatureCollection",
        "features": []
    }
    for string_node in string_nodes:
        index = find_feature(geojson["features"], 0, len(geojson["features"]) - 1, string_node)
        geojson_result["features"].append(geojson["features"][index])
    return geojson_result


    