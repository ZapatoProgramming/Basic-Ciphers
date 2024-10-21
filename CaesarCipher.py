# bruteforce attack to caesar cipher

def caesarCipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
    return result

def bruteForceAttack(text):
    for i in range(26):
        print("Shift: ", i, "Text: ", caesarCipher(text, i))

# Texto cifrado
plaintext = "MEETMEAFTERTHETOGAPARTY"
shift = 3
ciphertext = caesarCipher(plaintext, shift)
print("Ciphertext: ", ciphertext)
bruteForceAttack(ciphertext)
