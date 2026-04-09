from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route()
def home()
    return 💅 Edmonton Nail Salon Chatbot is running!

@app.route(chat, methods=[POST])
def chat()
    user_message = request.json.get(message).lower()

    if hello in user_message or hi in user_message
        reply = Hi 👋 Welcome to Edmonton Nail Salon! How can we help you today
    elif price in user_message or cost in user_message
        reply = (
            💅 Our demo prices (total ~$50)n
            - Manicure $20n
            - Pedicure $20n
            - Nail art $10
        )
    elif hour in user_message or open in user_message
        reply = 🕒 We are open from 10 AM to 8 PM, Monday to Sunday.
    elif address in user_message or location in user_message
        reply = 📍 We are located at 123 Demo Street, Edmonton, AB, Canada.
    elif book in user_message or appointment in user_message
        reply = (
            📅 You can book by calling us at (780) 555-1234 
            or message here with your preferred time!
        )
    else
        reply = Sorry 😅 I didn’t understand. You can ask about price, hours, or booking!

    return jsonify({reply reply})

if _name_ == _main_
    app.run(host=0.0.0.0, port=5000)
