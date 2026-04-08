# app.py

from flask import Flask, render_template, request, redirect, session, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import os
from utils.crypto import encrypt_aes, decrypt_aes, generate_key, caesar_encrypt, caesar_decrypt
from utils.steganography import encode_image, decode_image
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup (for user management and history)
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, user TEXT, action TEXT, result TEXT)
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper function to fetch history from the database
def get_history(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT action, result FROM history WHERE user=?", (user,))
    data = c.fetchall()
    conn.close()
    return data

# Home route (Login)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid credentials", 401

    return render_template("login.html")

# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("register.html")

# Dashboard route
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/")

    result = ""
    key = ""
    history = get_history(session["user"])

    if request.method == "POST":
        try:
            text = request.form["text"]
            mode = request.form["mode"]
            if mode == "aes":
                key = generate_key().decode()
                result = encrypt_aes(text, key.encode())
            elif mode == "caesar":
                shift = int(request.form["shift"])
                result = caesar_encrypt(text, shift)

            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("INSERT INTO history(user, action, result) VALUES (?,?,?)", (session["user"], mode, result))
            conn.commit()
            conn.close()

        except Exception as e:
            result = str(e)

    return render_template("dashboard.html", result=result, key=key, history=history)

# AES Key download route
@app.route("/download_key/<key>")
def download_key(key):
    path = "uploads/key.txt"
    with open(path, "w") as f:
        f.write(key)
    return send_file(path, as_attachment=True)

# File upload and encryption route
@app.route("/file", methods=["POST"])
def encrypt_file():
    if "user" not in session:
        return redirect("/")

    try:
        file = request.files["file"]
        filename = secure_filename(file.filename)
        if not filename:
            raise ValueError("Invalid file name")

        upload_root = os.path.abspath("uploads")
        filepath = os.path.abspath(os.path.join(upload_root, filename))
        if os.path.commonpath([upload_root, filepath]) != upload_root:
            raise ValueError("Invalid file path")

        file.save(filepath)

        key = generate_key()
        f = Fernet(key)

        with open(filepath, "rb") as f_in:
            data = f_in.read()

        encrypted_data = f.encrypt(data)

        encrypted_path = filepath + ".enc"
        with open(encrypted_path, "wb") as f_out:
            f_out.write(encrypted_data)

        return render_template("dashboard.html", file_result="File encrypted successfully!", download_file=encrypted_path)

    except Exception as e:
        return render_template("dashboard.html", file_result=f"Error: {str(e)}")

# Route for downloading encrypted files
@app.route("/download/<path:filename>")
def download_file(filename):
    return send_file(filename, as_attachment=True)

# Steganography routes (encode & decode)
@app.route("/encode", methods=["POST"])
def encode():
    file = request.files["image"]
    msg = request.form["secret"]

    filename = secure_filename(file.filename)
    if not filename:
        return render_template("dashboard.html", steg_result="Error: Invalid filename")

    upload_root = os.path.abspath("uploads")
    path = os.path.abspath(os.path.join(upload_root, filename))
    if os.path.commonpath([upload_root, path]) != upload_root:
        return render_template("dashboard.html", steg_result="Error: Invalid upload path")

    file.save(path)

    output = encode_image(path, msg)
    return render_template("dashboard.html", steg_result=f"Saved: {output}")

@app.route("/decode", methods=["POST"])
def decode():
    file = request.files["image"]

    upload_root = os.path.abspath("uploads")
    filename = secure_filename(file.filename)
    if not filename:
        return render_template("dashboard.html", steg_result="Error: Invalid filename.")

    path = os.path.abspath(os.path.join(upload_root, filename))
    if os.path.commonpath([upload_root, path]) != upload_root:
        return render_template("dashboard.html", steg_result="Error: Invalid file path.")

    file.save(path)

    msg = decode_image(path)
    return render_template("dashboard.html", steg_result=f"Message: {msg}")

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
