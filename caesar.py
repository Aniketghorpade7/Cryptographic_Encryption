def caesar_encrypt(text, shift=3):
    result = ""
    shift = int(shift)
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_verify(ciphertext, guess_shift, original_text):
    try:
        guess_shift = int(guess_shift)
        decrypted = caesar_encrypt(ciphertext, -guess_shift)
        return decrypted == original_text
    except Exception:
        return False
