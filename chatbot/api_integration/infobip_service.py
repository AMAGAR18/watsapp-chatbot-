import requests
from chatbot.config import BASE_URL , API_KEY , SENDER


def send_message(to, message) :
    url =  f"{BASE_URL}/whatsapp/1/message/text"
    headers = {"Authorization": f"App {API_KEY}"}
    payload = {
        "from":SENDER,
        "to":to,
        "content" : {"text" : message}

    }
    response = requests.post(url, json=payload , headers=headers)
    return response.status_code, response.text

def receive_message(incoming_data)  :
    """ Extract incoming messages"""
    messages= []
    for message in incoming_data.get("messages" , []) :
        messages.append({
            "from" : message["from"] ,
            "text" : message["text"]["body"]

        })
        return messages
