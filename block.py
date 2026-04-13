def block_xor_encrypt(text, key=123):
    key = int(key)
    return [ord(char) ^ key for char in text]

def block_xor_verify(ciphertext_blocks, guess_key, original_text):
    try:
        guess_key = int(guess_key)
        decrypted_chars = [chr(block ^ guess_key) for block in ciphertext_blocks]
        decrypted_text = "".join(decrypted_chars)
        return decrypted_text == original_text
    except Exception:
        return False

