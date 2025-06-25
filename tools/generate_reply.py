TOOL_NAME = "Antwortgenerator"
TOOL_DESC = "Generiert Bestätigungsmail basierend auf die Bestellung"
TOOL_USAGE = "ORDER"

def run(order_data: dict):
    return f"""
Hallo {order_data['name']},

vielen Dank für Ihre Bestellung von {order_data['quantity']}x {order_data['product']}.

Ihre Lieferung erfolgt am {order_data['delivery_date']} an:

{order_data['delivery_address']}

Sollte etwas nicht stimmen, antworten Sie gerne direkt auf diese Mail.

Beste Grüsse,
Ihr Shop-Team
"""