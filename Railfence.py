def print_rails(matrix):
    for row in matrix:
        print(' '.join(row))

def rail_fence_decrypt(ciphertext, K):
    # Inicializar la matriz vacía
    rail = [[' ' for i in range(len(ciphertext))] for j in range(K)]
    
    # Marcar las posiciones en las que las letras estarán basadas en K
    dir_down = None
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == K - 1:
            dir_down = False

        # Colocar marcador "*"
        rail[row][col] = '*'
        col += 1

        # Determinar la dirección
        if dir_down:
            row += 1
        else:
            row -= 1

    # Rellenar los marcadores con el ciphertext
    index = 0
    for i in range(K):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    print("Railfence (visualización):")
    print_rails(rail)

    # Leer el mensaje desencriptado usando el patrón rail
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == K - 1:
            dir_down = False

        # Recoger las letras en el orden correcto
        if rail[row][col] != ' ':
            result.append(rail[row][col])
            col += 1

        # Cambiar de fila según la dirección
        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)

# Pedir input al usuario
ciphertext = input("Introduce el ciphertext: ")
K = int(input("Introduce la clave (K): "))

# Desencriptar el ciphertext
decrypted_message = rail_fence_decrypt(ciphertext, K)
print("\nMensaje desencriptado:", decrypted_message)

