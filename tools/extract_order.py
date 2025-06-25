TOOL_NAME = "Bestellungs-Parser"
TOOL_DESC = "Extrahiert Name, Produkt, Menge usw. aus der Mail"
TOOL_USAGE = "ORDER"

from llm import ask_ollama
import json
import re

def run(mail_text: str) -> dict:
    prompt = f"""
# Aufgabe
Deine Aufgabe ist es, Informationen aus einem Text zu extrahieren.

# Bedingungen
Das Extrakt soll folgendes JSON-Format beinhalten:

{{
  "name": "...",
  "email": "...",
  "product": "...",
  "quantity": ...,
  "delivery_date": "...",
  "delivery_address": "..."
}}

# Input
Extrahiere die Informationen in ein JSON aus folgendem Mail:

\"\"\"
{mail_text}
\"\"\"

Gib das Ergebnis nur als JSON zurück ohne Markdown oder Erklärungen.
"""
    raw = ask_ollama(prompt)
    raw = re.sub(r"^```json", "", raw, flags=re.IGNORECASE).strip()
    result = re.sub(r"```$", "", raw).strip()

    try:
        print("Extrahierte Bestellung: ", result)
        return json.loads(result)
    except json.JSONDecodeError as e:
        json_match = re.search(r"\{[\s\S]+?\}", raw)
        if json_match:
            try:
                return json.loads(json_match.group())
            except Exception:
                pass  # fällt durch
        raise ValueError(f"JSON konnte nicht geparsed werden:\n{result}") from e