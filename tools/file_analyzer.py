def run(path):
    path = input("Pfad zur Datei:\n> ")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return "ERROR: Datei nicht gefunden."
    
    lines = content.splitlines()
    todos = [line for line in lines if 'TODO' in line.upper()]
    return f"""Datei Analyse:
- Wörter insgesamt: {len(content.split())}
- Zeilen: {len(lines)}
- TODOS gefunden: {len(todos)}
- Erste Zeile {lines[0] if lines else "(leer)"}"""

TOOL_NAME = "Datei"
TOOL_DESC = "Analysiert Textdateien"