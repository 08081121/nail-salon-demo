from flask import Flask, request, jsonify
import os  # để lấy PORT từ environment Render

# ✅ Tạo app Flask chính xác _name_
app = Flask(_name_)

# Route chính để kiểm tra app chạy live
@app.route("/")
def home():
    return "💅 Edmonton Nail Salon Chatbot is running!"

# Route chatbot demo
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # lấy JSON từ POST
    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message in JSON format."})

    user_message = data["message"].lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hi 👋 Welcome to Edmonton Nail Salon! How can we help you today?"
    elif "price" in user_message or "cost" in user_message:
        reply = (
            "💅 Our demo prices (total ~$50):\n"
            "- Manicure: $20\n"
            "- Pedicure: $20\n"
            "- Nail art: $10"
        )
    elif "hour" in user_message or "open" in user_message:
        reply = "🕒 We are open from 10 AM to 8 PM, Monday to Sunday."
    elif "address" in user_message or "location" in user_message:
        reply = "📍 We are located at 123 Demo Street, Edmonton, AB, Canada."
    elif "book" in user_message or "appointment" in user_message:
        reply = (
            "📅 You can book by calling us at (780) 555-1234 "
            "or message here with your preferred time!"
        )
    else:
        reply = "Sorry 😅 I didn’t understand. You can ask about price, hours, or booking!"

    return jsonify({"reply": reply})

# Chạy app trên Render
if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))  # lấy port Render cấp
    app.run(host="0.0.0.0", port=port)
