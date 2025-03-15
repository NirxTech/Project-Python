def encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def decode(encoded_text, shift):
    return encode(encoded_text, -shift)

# Contoh penggunaan
if __name__ == "__main__":
    text = input("Masukkan teks yang ingin di-encode: ")
    shift = int(input("Masukkan nilai shift (misalnya 3): "))

    encoded = encode(text, shift)
    print(f"Hasil Encode: {encoded}")

    decoded = decode(encoded, shift)
    print(f"Hasil Decode: {decoded}")
