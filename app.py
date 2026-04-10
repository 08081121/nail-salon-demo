from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

SALON_NAME = "Luxury Nail Studio 💅"
PHONE = "+1 604-123-4567"
ADDRESS = "123 Beauty Street, Vancouver, BC"

# ===== DATABASE =====
def init_db():
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html", salon=SALON_NAME, phone=PHONE, address=ADDRESS)

# ===== BOOKING =====
@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    time = data.get("time")

    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, phone, time) VALUES (?, ?, ?)", (name, phone, time))
    conn.commit()
    conn.close()

    return jsonify({"msg": "✅ Booking confirmed! We will contact you soon."})

# ===== ADMIN =====
@app.route("/admin")
def admin():
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("SELECT * FROM bookings ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    return render_template("admin.html", bookings=rows)

# ===== DELETE =====
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("DELETE FROM bookings WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
