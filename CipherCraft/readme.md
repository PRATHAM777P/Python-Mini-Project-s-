# 🔐 CipherCraft Pro – Secure Encryption & Steganography Suite

CipherCraft Pro is a **Flask-based web application** that provides secure text and file encryption along with image steganography. It supports multiple encryption techniques, user authentication, history tracking, and a modern UI.

---

## 🚀 Features

### 🔐 Encryption

* AES Encryption (secure key-based encryption)
* Caesar Cipher (basic shift cipher)
* Text encryption & decryption support

### 📁 File Security

* Upload and encrypt files
* Download encrypted files
* File decryption support

### 🔑 Key Management

* Auto-generate AES keys
* Display encryption key after processing
* Download key as a file

### 👤 Authentication System

* User Registration & Login
* Password hashing using bcrypt
* Session-based authentication

### 📜 History Tracking

* Stores past encryption operations
* Displays history on dashboard
* Uses SQLite database

### 🖼 Steganography

* Hide secret messages inside images
* Extract hidden messages from images

### 🎨 User Interface

* Responsive UI using Bootstrap
* Clean dashboard layout
* Dark mode toggle 🌙

### ⚠️ Error Handling

* Input validation
* Safe file handling
* Exception handling for all operations

---

## 🏗 Project Structure

```
CipherCraft-Pro/
│
├── app.py
├── database.db
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│
├── static/
│   └── (optional CSS/JS files)
│
├── utils/
│   ├── crypto.py
│   ├── steganography.py
│
└── uploads/
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/ciphercraft-pro.git
cd ciphercraft-pro
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment (Render)

1. Push project to GitHub
2. Go to Render
3. Create new Web Service
4. Add:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn app:app`
5. Deploy 🚀

---

## 🔮 Future Improvements

* RSA encryption
* Cloud storage (AWS / Firebase)
* REST API integration
* React frontend
* Advanced steganography (audio/video)

---

## 🏆 Project Highlights

* Full-stack Flask application
* Real-world encryption techniques
* Secure authentication system
* File handling + steganography
* Deployment-ready

---

