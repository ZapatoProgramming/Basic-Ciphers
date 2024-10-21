def vigenere_cipher(text, key):
    result = ""
    key = key.lower()  # Asegurar que la clave esté en minúsculas
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():  # Solo cifrar letras
            shift = ord(key[i % len(key)]) - ord('a')
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char  # Dejar otros caracteres sin cambios
    return result

# Texto cifrado
plaintext = "wearediscoveredsaveyourself"
key = "deceptive"
ciphertext = vigenere_cipher(plaintext, key)
print("Ciphertext: ", ciphertext)
