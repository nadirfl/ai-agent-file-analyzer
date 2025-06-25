from tools import load_csv, validate_data, analyze_data, notify_user
from llm import ask_ollama

def run_workflow():
    print("Starte Workflow")
    print("---------------")

    try:
        df = load_csv.run(None)
        validate_data.run(df)
        result = analyze_data.run(df)
        print("Analyse abgeschlossen: ", result)
    
    except Exception as e:
        print("Fehler erkannt: ", str(e))

        decision_prompt = f"""
Im aktuellen Workflow ist ein Fehler aufgetreten:
\"{str(e)}\"

Was soll der Agent tun?
Mögliche Optionen:
- USER_BENACHRICHTIGEN
- ABBRECHEN

Gib exakt nur den Aktionscode aus.
"""
        
        action = ask_ollama(decision_prompt)
        print(f"LLM-Entscheidung: {action}")

        if action == "USER_BENACHRICHTIGEN":
            print(notify_user.run(str(e)))
        elif action == "ABBRECHEN":
            print("Workflow wird beendet")
        else:
            print(f"Unbekannte Anweisung vom LLM: {action}")

if __name__ == "__main__":
    run_workflow()