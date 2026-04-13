# 🔐 Cryptography Visualizer (Step-by-Step Encryption & Decryption)

---

## 📌 Project Overview

The **Cryptography Visualizer** is an educational web application designed to demonstrate how different cryptographic algorithms work internally.

Instead of only showing input and output, this system **explains each step of encryption and decryption**, making it easier to understand the underlying mathematical concepts.

---

## 🎯 Objective

* To visualize cryptographic algorithms
* To explain **how encryption and decryption actually happen**
* To bridge the gap between theory and implementation
* To make complex mathematical concepts easy to understand

---

## 🚀 Features

* 🔐 Supports **3 Levels of Cryptography**

  * 🟢 Easy → Caesar Cipher
  * 🟡 Medium → XOR (Block Cipher Concept)
  * 🔴 Hard → RSA

* 🧠 Step-by-step explanation system

* 🔄 Shows both **encryption and decryption process**

* 🎨 Modern UI with hover effects and transitions

* ⚡ Interactive user input

---

## 🧠 Mathematical Concepts Used

### 🟢 Caesar Cipher

* Modular arithmetic
* Formula:

  C = (P + k) mod 26
  P = (C - k) mod 26

---

### 🟡 XOR Cipher (Block Concept)

* Bitwise operations

* Formula:

  C = P ⊕ K

* Key property:

  P = C ⊕ K

(XOR is reversible)

---

### 🔴 RSA Algorithm

* Number theory
* Prime numbers
* Modular arithmetic

Key formulas:

n = p × q
φ(n) = (p − 1)(q − 1)

Encryption:
c = m^e mod n

Decryption:
m = c^d mod n

---

## 🔄 How It Works

1. User enters a message
2. Selects security level
3. System performs encryption
4. Step-by-step explanation is shown
5. Decryption process is demonstrated
6. Original message is recovered

---

## 🎨 UI & Interaction

* Dark theme modern design
* Smooth transitions between steps
* “Next” button reveals each stage
* Clear separation of encryption and decryption

---

## 📁 Project Structure

crypto_visualizer/
│
├── app.py → Backend logic (Flask)
├── rsa_core.py → RSA algorithm implementation
└── templates/
  └── index.html → UI + step visualization

---

## 🛠️ Tech Stack

* Python
* Flask
* HTML
* CSS
* JavaScript

---

## ▶️ How to Run

### 1. Navigate to project folder

cd crypto_visualizer

---

### 2. Create virtual environment (optional)

python -m venv venv
source venv/bin/activate

---

### 3. Install dependencies

pip install flask

---

### 4. Run the app

python app.py

---

### 5. Open in browser

http://127.0.0.1:5000

---

## 🎤 Viva Explanation (Short)

“This project visualizes encryption and decryption processes across different cryptographic techniques. It breaks down each step mathematically to help users understand how secure communication works.”

---

## 🎤 Viva Explanation (Detailed)

“This system demonstrates three levels of cryptographic techniques, starting from simple modular arithmetic in Caesar Cipher, moving to bitwise operations in XOR, and finally to number theory in RSA. Each algorithm is explained step-by-step, showing both encryption and decryption to provide complete conceptual clarity.”

---

## 💡 Key Learning Outcomes

* Understanding encryption vs decryption
* Application of mathematical concepts in security
* Modular arithmetic and number theory
* Bitwise operations (XOR)
* Building interactive web applications

---

## 🔮 Future Enhancements

* 📊 Graphical visualization of transformations
* 🎬 Animated transitions between steps
* 🔐 Real-world cryptographic standards (AES)
* 🌐 Deployment on web

---

## 👩‍💻 Author

Developed as part of an **Engineering Mathematics & Cryptography Project** to demonstrate real-world applications of mathematical concepts.

- Gajanan Domatwar
- Pratiksha Bade
- Aniket Ghorpade

---
