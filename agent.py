from llm import ask_ollama
from tool_manager import load_tools

tools = load_tools(usage_filter="AGENT")

def main():
    print("AI-Agent gestartet")
    print("------------------")

    print("Folgende Tools stehen zur Verfügung: ")
    for t in tools.values():
        print(f" - {t['name']}: {t['desc']}")

    while True:
        user_input = input("Was soll ich tun?\n> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Beende Session")
            break

        tool_list_str = "\n".join([f"- {t['name']}: {t['desc']}" for t in tools.values()])

        decision_prompt = f"""
Du bist ein Agent mit den folgenden Tools:

{tool_list_str}

Basierend auf dieser Benutzeranfrage:
\"{user_input}\""

Welches Tool soll verwendet werden? Gib exakt den Toolnamen zurück.
"""

        decision = ask_ollama(decision_prompt).lower()

        print("Decision Prompt Output: ", decision)

        for key, tool in tools.items():
            if decision in tool["name"].lower():
                print("Folgendes Tool wurde gewählt: ", tool["name"])
                result = tool["run"](user_input)
                print("Ergebnis: ", result)
                break    
        else:
            print("Ich bin mir unsicher, versuche direkte Antwort zu geben...")
            answer = ask_ollama(user_input)
            print("💬 LLM:", answer)

if __name__ == "__main__":
    main()