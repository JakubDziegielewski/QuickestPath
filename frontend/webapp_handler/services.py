from src.app import App
def process_text_list(text_list, app: App):
    # Example processing: convert all texts to uppercase
    processed_list = [text for text in text_list]
    l = app.run_query(processed_list)
    s = [str(x) for x in l]
    result = ", ".join(s)
    return "(node(id:" + result + ")({{bbox}}););out body;"
