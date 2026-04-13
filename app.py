from flask import Flask, render_template, request, jsonify
import caesar
import block
import rsa_enc

app = Flask(__name__, template_folder='frontend')
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def api_start():
    data = request.json
    msg = data.get("message", "")
    level = data.get("level")

    if level == "easy":
        k = int(data.get("k", 3))
        res = caesar.caesar_encrypt(msg, shift=k)

        # Build per-character encryption detail
        char_enc_details = []
        for ch in msg:
            if ch.isalpha():
                p_val = ord(ch.upper()) - ord('A')
                c_val = (p_val + k) % 26
                enc_ch = chr(c_val + ord('A') if ch.isupper() else c_val + ord('a'))
                char_enc_details.append(f"'{ch}' → ({p_val} + {k}) mod 26 = {c_val} → '{enc_ch}'")
            else:
                char_enc_details.append(f"'{ch}' → unchanged")

        char_dec_details = []
        for ch in res:
            if ch.isalpha():
                c_val = ord(ch.upper()) - ord('A')
                p_val = (c_val - k) % 26
                dec_ch = chr(p_val + ord('A') if ch.isupper() else p_val + ord('a'))
                char_dec_details.append(f"'{ch}' → ({c_val} - {k}) mod 26 = {p_val} → '{dec_ch}'")
            else:
                char_dec_details.append(f"'{ch}' → unchanged")

        response_data = {
            "method": "Level 1: Caesar Cipher",
            "original": msg,
            "res": res,
            "key": k,
            "steps": [
                {
                    "t": "Step 1: Understand the Formula",
                    "d": f"Caesar Cipher shifts every letter by a fixed amount.\n\nEncryption: C = (P + k) mod 26\nDecryption: P = (C - k) mod 26\n\nYour secret key: k = {k}\nPlaintext: '{msg}'"
                },
                {
                    "t": "Step 2: Encrypt Each Character",
                    "d": "Applying C = (P + k) mod 26 to every letter:\n\n" + "\n".join(char_enc_details)
                },
                {
                    "t": "Step 3: Encryption Complete!",
                    "d": f"Plaintext:  '{msg}'\nCiphertext: '{res}'"
                }
            ],
            "decryption_steps": [
                {
                    "t": "Decryption: Reverse the Shift",
                    "d": f"To decrypt, we reverse the operation.\n\nFormula: P = (C - k) mod 26\nUsing key: k = {k}\nCiphertext: '{res}'"
                },
                {
                    "t": "Decrypt Each Character",
                    "d": "Applying P = (C - k) mod 26 to every letter:\n\n" + "\n".join(char_dec_details)
                },
                {
                    "t": "Decryption Result",
                    "d": f"Ciphertext: '{res}'\nRecovered:  '{msg}'\n\nNow guess the key to prove you cracked the code!"
                }
            ]
        }

    elif level == "medium":
        raw_key = data.get("key", "42")
        if str(raw_key).isdigit():
            key = int(raw_key)
        elif len(str(raw_key)) == 1:
            key = ord(str(raw_key))
        else:
            return jsonify({"error": "XOR key must be a 1-2 digit number or a single character."}), 400

        res = block.block_xor_encrypt(msg, key=key)

        char_enc_details = []
        for i, ch in enumerate(msg):
            ascii_val = ord(ch)
            enc_val = res[i]
            char_enc_details.append(f"'{ch}' → ASCII {ascii_val} XOR {key} = {enc_val}")

        char_dec_details = []
        for i, enc_val in enumerate(res):
            dec_val = enc_val ^ key
            dec_ch = chr(dec_val)
            char_dec_details.append(f"{enc_val} XOR {key} = {dec_val} → '{dec_ch}'")

        response_data = {
            "method": "Level 2: Block XOR",
            "original": msg,
            "res": res,
            "key": key,
            "steps": [
                {
                    "t": "Step 1: XOR Cipher Explained",
                    "d": f"XOR is a bitwise operation. It flips bits based on a key.\n\nEncryption: C = P ⊕ K\nDecryption: P = C ⊕ K  (XOR is self-reversing!)\n\nYour secret key: K = {key}\nPlaintext: '{msg}'"
                },
                {
                    "t": "Step 2: Encrypt Each Character",
                    "d": "Applying C = P ⊕ K to every character:\n\n" + "\n".join(char_enc_details)
                },
                {
                    "t": "Step 3: Encryption Complete!",
                    "d": f"Plaintext: '{msg}'\nCiphertext blocks: {res}"
                }
            ],
            "decryption_steps": [
                {
                    "t": "Decryption: XOR is Self-Reversing!",
                    "d": f"Because XOR is its own inverse:\n\nP = C ⊕ K\n\nApplying the same key K = {key} to the cipher decrypts it.\nCiphertext: {res}"
                },
                {
                    "t": "Decrypt Each Block",
                    "d": "Applying P = C ⊕ K to every block:\n\n" + "\n".join(char_dec_details)
                },
                {
                    "t": "Decryption Result",
                    "d": f"Ciphertext blocks: {res}\nRecovered text:    '{msg}'\n\nNow guess the key to prove you cracked it!"
                }
            ]
        }

    elif level == "hard":
        try:
            p = int(data.get("p"))
            q = int(data.get("q"))
            pub, priv, p, q, phi = rsa_enc.generate_keys_from_primes(p, q)
            res = rsa_enc.rsa_encrypt(msg, pub)
            e, n = pub
            d, _ = priv

            char_enc_details = []
            for i, ch in enumerate(msg):
                m = ord(ch)
                c = res[i]
                char_enc_details.append(f"'{ch}' → m={m} → {m}^{e} mod {n} = {c}")

            char_dec_details = []
            for c_val in res[:min(3, len(res))]:
                m = pow(c_val, d, n)
                char_dec_details.append(f"{c_val}^{d} mod {n} = {m} → '{chr(m)}'")
            if len(res) > 3:
                char_dec_details.append("... (same process for all blocks)")

            response_data = {
                "method": "Level 3: RSA Encryption",
                "original": msg,
                "res": res,
                "public_key": list(pub),
                "private_key": list(priv),
                "steps": [
                    {
                        "t": "Step 1: RSA Key Generation",
                        "d": f"Choose two distinct primes p and q:\np = {p},  q = {q}\n\nn = p × q = {p} × {q} = {n}\nφ(n) = (p-1)(q-1) = {p-1} × {q-1} = {phi}"
                    },
                    {
                        "t": "Step 2: Public & Private Keys",
                        "d": f"Find e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1:\ne = {e}\n\nFind d such that (e × d) mod φ(n) = 1:\nd = {d}\n\nPublic Key:  (e={e}, n={n})\nPrivate Key: (d={d}, n={n})"
                    },
                    {
                        "t": "Step 3: Encrypt Each Character",
                        "d": "Applying C = M^e mod n for each character:\n\n" + "\n".join(char_enc_details)
                    },
                    {
                        "t": "Step 4: Encryption Complete!",
                        "d": f"Plaintext:  '{msg}'\nCiphertext: {res}"
                    }
                ],
                "decryption_steps": [
                    {
                        "t": "RSA Decryption Formula",
                        "d": f"Using the Private Key (d={d}, n={n}):\n\nFormula: M = C^d mod n\n\nOnly the private key d can decrypt!"
                    },
                    {
                        "t": "Decrypt Each Block",
                        "d": "Applying M = C^d mod n to first few blocks:\n\n" + "\n".join(char_dec_details)
                    },
                    {
                        "t": "Decryption Complete!",
                        "d": f"Recovered: '{msg}'\n\nThe private exponent d = {d}.\nGuess d to prove you cracked RSA!"
                    }
                ]
            }
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    return jsonify(response_data)



@app.route("/api/guess_decrypt", methods=["POST"])
def api_guess():
    data = request.json
    level = data.get("level")
    ciphertext = data.get("res")
    original = data.get("original")
    guess = data.get("guess")

    success = False
    if level == "easy":
        success = caesar.caesar_verify(ciphertext, guess, original)
    elif level == "medium":
        raw_guess = str(guess)
        if raw_guess.isdigit():
            guess_val = int(raw_guess)
        elif len(raw_guess) == 1:
            guess_val = ord(raw_guess)
        else:
            guess_val = None
        success = block.block_xor_verify(ciphertext, guess_val, original) if guess_val is not None else False
    elif level == "hard":
        pub = data.get("public_key")
        correct_d = data.get("correct_d")
        success = rsa_enc.rsa_verify(ciphertext, guess, correct_d, pub, original)

    if success:
        return jsonify({"status": "success", "message": f"ACCESS GRANTED! The original message '{original}' has been recovered!"})
    else:
        return jsonify({"status": "error", "message": "ACCESS DENIED. Decryption failed. Try again!"})

if __name__ == "__main__":
    app.run(debug=True)