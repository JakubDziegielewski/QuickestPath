import requests
from xml.etree import ElementTree as ET
import json
from src.app import App
def process_text_list(text_list, app: App):
    # Example processing: convert all texts to uppercase
    processed_list = [text for text in text_list]
    l = app.run_query(processed_list)
    s = [str(x) for x in l]
    result = ", ".join(s).replace('\n', '')
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
            "properties": {},
            "geometry": {
                "type": "Point",
                "coordinates": [float(node.get('lon')), float(node.get('lat'))]
            }
        }

        # Add properties if available
        for tag in node.findall('tag'):
            feature["properties"][tag.get('k')] = tag.get('v')

        geojson["features"].append(feature)
    with open('geo2.geojson', 'w') as f:
        json.dump(geojson, f, indent=2)
    return geojson
