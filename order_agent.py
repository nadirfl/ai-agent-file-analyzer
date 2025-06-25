from tool_manager import load_tools

tools = load_tools("ORDER")

classify = tools["classify_mail"]["run"]
extract = tools["extract_order"]["run"]
store = tools["store_order"]["run"]
reply = tools["generate_reply"]["run"]
notify = tools["notify_user"]["run"]

def run_order_agent(mail_path: str):
    with open(mail_path, "r", encoding="utf-8") as f:
        mail_text = f.read()

    print("Mail geladen. Klassifiziere...")

    category = classify(mail_text)
    print(f"Kategorie: {category}")

    if category == "INFO":
        print(notify("Mail als INFO erkannt. Kein Handlungsbedarf"))
    elif category == "TODO":
        print(notify("Mail als TODO erkannt. Bitte manuell überprüfen"))
    elif category == "AUTO":
        data = extract(mail_text)
        print(store(data))
        confirmation = reply(data)

        with open("output/reply_mail.txt", "w", encoding="utf-8") as f:
            f.write(confirmation)
        print("Antwortmail generiert")
    else:
        print("Unbekannte Kategorie: ", category)

if __name__ == "__main__":
    run_order_agent("mails/mail_001.txt")
