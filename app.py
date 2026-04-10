from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

SALON_INFO = """
💅 Nail Salon AI

📍 Address:
123 Beauty Street, Vancouver, BC, Canada

📞 Phone:
+1 604-123-4567

💰 Prices:
- Manicure: $20
- Pedicure: $25
- Gel Nails: $35
- Nail Art: from $5+

📅 Booking: Tell me what day & time you want
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message"})

    msg = data["message"].lower()

    if "hi" in msg or "hello" in msg:
        reply = "Hello 👋 Welcome to Nail Salon 💅\n\n" + SALON_INFO

    elif "price" in msg:
        reply = "💰 Here are our prices:\n\n" + SALON_INFO

    elif "phone" in msg or "contact" in msg:
        reply = "📞 Contact us:\n\n" + SALON_INFO

    elif "address" in msg or "where" in msg:
        reply = "📍 Our location:\n\n" + SALON_INFO

    elif "book" in msg:
        reply = "📅 Sure! Please tell me your preferred date and time 😊"

    elif "service" in msg:
        reply = "💅 We offer manicure, pedicure, gel nails, nail art!"

    else:
        reply = "💅 I can help you with booking, prices, address, and phone number."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
