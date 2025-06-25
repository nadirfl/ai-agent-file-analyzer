TOOL_NAME = "DB-Speicher"
TOOL_DESC = "Speichert Bestellung als JSON"
TOOL_USAGE = "ORDER"

import json
import os

def run(data:dict):
    os.makedirs("output", exist_ok=True)
    path = "output/orders.json"

    db = []
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r", encoding="utf-8") as f:
            try:
                db = json.load(f)
            except json.JSONDecodeError:
                print("orders.json ist ungültig, wird überschrieben")
                db = []
    
    db.append(data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    
    return "Bestellung gespeichert"