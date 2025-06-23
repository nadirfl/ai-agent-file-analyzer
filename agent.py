from llm import ask_ollama
from tools.file_analyzer import analyze_file
from tools.summarize import summarize_text

def main():
    print("AI-Agent gestartet")

    while True:
        user_input = input("Was soll ich tun?\n> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Beende Session")
            break

        decision_prompt = (
            "Du bist ein Agent mit den Tools:\n"
            "- datei: analysiert Textdateien\n"
            "- zusammenfassen: fasst Texte zusammen\n"
            "Nenne nur das passende Tool für die folgende Anfrage:\n"
            f"{user_input}"
        )

        decision = ask_ollama(decision_prompt).lower()

        print("Decision Prompt Output: ", decision)

        if "datei" in decision:
            path = input("Pfad zur Datei:\n> ")
            result = analyze_file(path)
            print(result)
        elif "zusammenfassen" in user_input.lower():
            text = input("Text eingeben:\n> ")
            summary = summarize_text(text)
            print("Tool-Antwort: ", summary)
        else:
            print("Ich bin mir unsicher, versuche direkte Antwort zu geben...")
            answer = ask_ollama(user_input)
            print("💬 LLM:", answer)

if __name__ == "__main__":
    main()