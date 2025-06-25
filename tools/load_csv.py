import os
import pandas as pd

def run(_):
    path = "data.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Datei '{path}' nicht gefunden")
    df = pd.read_csv(path)
    return df

TOOL_NAME = "Datenimport"
TOOL_DESC = "Lädt eine definierte Datei ein"
TOOL_USAGE = "WORKFLOW"