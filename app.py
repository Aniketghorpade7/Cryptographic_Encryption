# from flask import Flask, render_template, request
# from rsa_core import *

# app = Flask(__name__)

# def caesar_encrypt(text, k):
#     return ''.join([chr((ord(c)-65+k)%26 + 65) for c in text])

# def caesar_decrypt(text, k):
#     return ''.join([chr((ord(c)-65-k)%26 + 65) for c in text])

# @app.route("/", methods=["GET", "POST"])
# def home():
#     data = {}

#     if request.method == "POST":
#         msg = request.form["message"].upper()
#         level = request.form["level"]

#         if level == "easy":
#             k = 3
#             cipher = caesar_encrypt(msg, k)
#             plain = caesar_decrypt(cipher, k)

#             steps = [
#                 "Convert letters to numbers (A=0...Z=25)",
#                 "Apply formula C = (P + k) mod 26",
#                 f"Encrypted text: {cipher}",
#                 "Apply formula P = (C - k) mod 26",
#                 f"Decrypted text: {plain}"
#             ]

#         elif level == "medium":
#             key = 5
#             cipher = ''.join([chr(ord(c) ^ key) for c in msg])
#             plain = ''.join([chr(ord(c) ^ key) for c in cipher])

#             steps = [
#                 "Convert text to ASCII values",
#                 "Apply XOR with key",
#                 f"Encrypted text: {cipher}",
#                 "Apply XOR again (reversible)",
#                 f"Decrypted text: {plain}"
#             ]

#         else:
#             public, private, p, q, phi = generate_keys()
#             cipher = encrypt(msg, public)
#             plain = decrypt(cipher, private)

#             steps = [
#                 f"Choose primes p={p}, q={q}",
#                 f"Compute n={public[1]}, φ(n)={phi}",
#                 f"Public key (e,n)={public}",
#                 f"Private key (d,n)={private}",
#                 f"Encrypt: {cipher}",
#                 f"Decrypt: {plain}"
#             ]

#         data = {"steps": steps}

#     return render_template("index.html", data=data)

# app.run(debug=True)








from flask import Flask, render_template, request
import Cryptographic_Encryption.rsa_core as rsa_core

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize default data to prevent "Undefined" errors in template
    data = {"steps": [], "original": "", "res": "", "method": ""}

    if request.method == "POST":
        msg = request.form.get("message", "")
        level = request.form.get("level")
        
        if level == "easy":
            res = rsa_core.caesar_encrypt(msg)
            data = {
                "method": "Level 1: Caesar Cipher",
                "original": msg,
                "res": res,
                "steps": [
                    {"t": "Step 1: Text to ASCII", "d": f"We take your message '{msg}' and look at the letters."},
                    {"t": "Step 2: The Shift", "d": "We slide each letter forward by 3 spots in the alphabet circle! "},
                    {"t": "Step 3: Encrypted!", "d": f"Your secret code is: {res}"}
                ]
            }
        elif level == "medium":
            res = rsa_core.block_xor_encrypt(msg)
            data = {
                "method": "Level 2: Block XOR",
                "original": msg,
                "res": str(res),
                "steps": [
                    {"t": "Step 1: Binary Split", "d": "We turn your message into numbers (ASCII codes)."},
                    {"t": "Step 2: XOR Magic", "d": "We use a secret key to flip the bits of your data! [cite: 63]"},
                    {"t": "Step 3: Scrambled!", "d": f"Output blocks: {res}"}
                ]
            }
        elif level == "hard":
            pub, priv, p, q, phi = rsa_core.generate_keys()
            res = rsa_core.rsa_encrypt(msg, pub)
            data = {
                "method": "Level 3: RSA Encryption",
                "original": msg,
                "res": str(res),
                "steps": [
                    {"t": "Step 1: Prime Keys", "d": f"We picked two secret primes: p={p} and q={q}."},
                    {"t": "Step 2: Public Key", "d": f"We calculate n = p * q ({pub[1]}) and e ({pub[0]}). [cite: 94]"},
                    {"t": "Step 3: Math Power", "d": "We use Modular Exponentiation: C = M^e mod n. [cite: 96]"},
                    {"t": "Step 4: Result", "d": f"The final ciphertext is: {res}"}
                ]
            }
            
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)