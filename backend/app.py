from flask import Flask, request, jsonify
from flask_cors import CORS

import mysql.connector

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="quiz_app"
    )

@app.route("/")
def home():
    return "Quiz App Backend is Running 🚀"


# 🔐 ADMIN LOGIN (POST)
@app.route("/admin/login", methods=["POST"])
def admin_login():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"status": "error", "message": "Username & password required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM admins WHERE username=%s AND password=%s",
        (username, password)
    )

    admin = cursor.fetchone()

    cursor.close()
    conn.close()

    if admin:
        return jsonify({
            "status": "success",
            "message": "Admin login successful"
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid admin credentials"
        }), 401


# 🎯 GET ONE QUESTION (LIVE QUIZ)
@app.route("/quiz/question", methods=["GET"])
def get_question():
    index = int(request.args.get("index", 0))
    category = request.args.get("category", "science")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT q.question_id, q.question,
               q.option_a, q.option_b, q.option_c, q.option_d,
               q.correct_option
        FROM questions q
        JOIN categories c ON q.category_id = c.category_id
        WHERE c.category_name = %s
        LIMIT 1 OFFSET %s
    """, (category, index))

    question = cursor.fetchone()

    cursor.close()
    conn.close()

    if question:
        return jsonify({
            "status": "success",
            "question": question
        })
    else:
        return jsonify({
            "status": "end",
            "message": "No more questions"
        })


# 🚀 START SERVER (ALWAYS LAST)
if __name__ == "__main__":
    app.run(debug=True)
