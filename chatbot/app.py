from flask import Flask, request
from chatbot.handlers.intent_handler import handle_intent, recognise_intent

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def process_message():
    user_message = request.json.get("message", "")
    intent = recognise_intent(user_message)
    response = handle_intent(intent, user_message)
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)
