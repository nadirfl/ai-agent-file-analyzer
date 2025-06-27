TOOL_NAME = "Mail-Klassifikation"
TOOL_DESC = "Klassifiziert Mails in INFO, TODO oder AUTO"
TOOL_USAGE = "ORDER"

from llm import ask_ollama

def run(mail_text: str) -> str:
    prompt = f"""
Du bist ein E-Mail-Klassifikator

Kategorien:
- INFO: irrelevante Mails wie Newsletter, Werbung
- AUTO: Bestellung (Produkt, Menge, Adresse erkennbar)
- TODO: unklar, braucht manuelle Bearbeitung

Welche Kategorien passt auf diese Mail?

Mail:
\"\"\"
{mail_text}
\"\"\"

Antworte zwingend nur mit einer der entsprechenden Kategorien: INFO, AUTO oder TODO
"""
    return ask_ollama(prompt)