from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# lưu lịch sử chat đơn giản (RAM)
chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Please send a message"})

    user_message = data["message"]

    chat_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly and professional nail salon assistant in Canada. You help customers with services, pricing, and booking appointments. Keep replies short, friendly, and helpful."
                }
            ] + chat_history[-10:]  # nhớ 10 tin gần nhất
        )

        reply = response.choices[0].message.content

        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        reply = "Server busy 😢 please try again"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
