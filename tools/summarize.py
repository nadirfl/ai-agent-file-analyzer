def run(text):
    return f"Der Text hat {len(text.split())} Wörter. Erste 100 Zeichen: {text[:100]}..."

TOOL_NAME = "Zusammenfassung"
TOOL_DESC = "Fasst einen beliebigen Text kurz zusammen."