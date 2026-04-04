
```
# 🔐 PassForge Pro – Advanced Password Generator

## 📌 Project Overview
**PassForge Pro** is a Python-based password generator with a **graphical user interface (GUI)** using **Tkinter**.  
It helps users create **strong, secure, and random passwords** with customizable options and added usability features.

This tool is ideal for anyone who wants to improve their password security quickly and easily.

---

## 🚀 Features
- 🔢 **Customizable Password Length** – choose the number of characters in your password.  
- 🔠 **Include Uppercase Letters** – for stronger passwords.  
- 🚫 **Avoid Confusing Characters** – excludes characters like `l`, `1`, `O`, and `0`.  
- 🧠 **Memorable Password Mode** – generates passwords using an adjective + noun + number combination.  
- 👁️ **Show / Hide Password** – toggle password visibility in the entry field.  
- 📋 **Copy Password to Clipboard** – easily copy generated passwords.  
- 💾 **Save Passwords to File** – stores passwords in `passwords.txt`.  
- 📊 **Password Strength Meter** – indicates how strong the generated password is.

---

## 🛠️ Technologies Used
- **Python 3.x**  
- **Tkinter** – for the GUI  
- **secrets module** – for cryptographically secure random generation  
- **string module** – for character sets

---

## 📂 Project Structure
```

PassForge-Pro/
│── main.py           # Main Python program
│── passwords.txt     # Generated passwords (created when saved)
│── README.md         # Project documentation

````

---

## ▶️ How to Run the Project
1. Make sure Python 3.x is installed on your system.  
2. Clone or download the repository:
```bash
git clone <repository-url>
````

3. Navigate to the project directory:

```bash
cd PassForge-Pro
```

4. Run the program:

```bash
python main.py
```

5. Use the GUI to generate, copy, and save passwords.

---

## 🖥️ GUI Usage

1. **Password Length:** Enter your desired length.
2. **Options:**

   * Include Uppercase Letters
   * Avoid Confusing Characters
   * Memorable Password (adjective + noun + number)
   * Show Password
3. **Generate Password:** Click to create a password.
4. **Copy / Save / Clear:** Use buttons to copy to clipboard, save to file, or clear the entry field.
5. **Password Strength:** Displays the strength of the generated password.

---

## 💡 Example Outputs

**Random Strong Password:**

```
G#7k!pZ@9LmQ
Strength: Very Strong
```

**Memorable Password Mode:**

```
bluepanda42
Strength: Medium
```

---

## 📈 Future Improvements

* 🌙 Dark mode / modern UI design
* 🌐 Web-based version using Flask or Django
* 🗂 Password manager / history
* 📊 Visual strength indicator graph
