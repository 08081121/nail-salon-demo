from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message"})

    user_message = data["message"].lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hello, welcome to our nail salon"
    elif "price" in user_message:
        reply = "Manicure is 20 dollars, Pedicure is 25 dollars"
    elif "hour" in user_message:
        reply = "We are open from 10 AM to 8 PM"
    else:
        reply = "Sorry, I do not understand"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
