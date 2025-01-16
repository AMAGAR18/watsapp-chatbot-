import os
import json

# Corrected path to products.json using absolute path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../products.json"))

# Load products.json
with open(file_path, "r") as f:
    products = json.load(f)

def recognise_intent(message):
    # Logic for recognising intent based on the user's message
    if "battery" in message.lower():
        return "filter_battery"
    elif "processor" in message.lower():
        return "filter_processor"
    elif "color" in message.lower():
        return "query_color"
    return "unknown"

def handle_intent(intent, message):
    if intent == "filter_battery":
        min_battery = 4000
        results = [product for product in products if product.get("battery_capacity", 0) >= min_battery]
        return f"Phones with battery capacity over {min_battery}mAh: {results}"
    elif intent == "filter_processor":
        if "under $800" in message.lower():
            results = [product for product in products if product.get("price", 0) < 800 and "Snapdragon" in product.get("processor", "")]
            return f"Devices with Snapdragon processors under $800: {results}"
    elif intent == "query_color":
        if "Galaxy S23" in message:
            product = next((product for product in products if product.get("name") == "Galaxy S23"), None)
            if product:
                return f"Available colors for Galaxy S23: {product.get('available_colors', [])}"
            return "Galaxy S23 not found."
    return "I'm not sure how to help with that."
