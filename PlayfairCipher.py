import string

# Función para preparar la clave y generar la matriz de 5x5
def generar_matriz(key):
    # Eliminar duplicados y mantener el orden en la clave
    key = "".join(sorted(set(key), key=key.index))
    
    # Combinar la clave y las letras restantes del alfabeto (excepto 'J', se sustituye por 'I')
    alfabeto = string.ascii_uppercase.replace('J', '')
    key_matrix = key + ''.join([c for c in alfabeto if c not in key])
    
    # Crear la matriz de 5x5
    matriz = [list(key_matrix[i:i + 5]) for i in range(0, 25, 5)]
    
    return matriz

# Función para preparar el texto plano
def preparar_texto(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    
    # Insertar 'X' entre letras repetidas y hacer longitud par
    resultado = []
    i = 0
    while i < len(text):
        resultado.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            resultado.append('X')
        i += 1
        if i < len(text):
            resultado.append(text[i])
        i += 1
    if len(resultado) % 2 != 0:
        resultado.append('X')
    
    return "".join(resultado)

# Función para encontrar la posición de una letra en la matriz
def encontrar_posicion(matriz, letra):
    for i, fila in enumerate(matriz):
        for j, char in enumerate(fila):
            if char == letra:
                return i, j
    return None

# Función para cifrar el texto
def cifrar_playfair(plaintext, matriz):
    plaintext = preparar_texto(plaintext)
    ciphertext = []
    
    # Procesar el texto en pares
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        fila1, col1 = encontrar_posicion(matriz, a)
        fila2, col2 = encontrar_posicion(matriz, b)
        
        # Caso 1: Si están en la misma fila
        if fila1 == fila2:
            ciphertext.append(matriz[fila1][(col1 + 1) % 5])
            ciphertext.append(matriz[fila2][(col2 + 1) % 5])
        
        # Caso 2: Si están en la misma columna
        elif col1 == col2:
            ciphertext.append(matriz[(fila1 + 1) % 5][col1])
            ciphertext.append(matriz[(fila2 + 1) % 5][col2])
        
        # Caso 3: Si forman un rectángulo
        else:
            ciphertext.append(matriz[fila1][col2])
            ciphertext.append(matriz[fila2][col1])
    
    return "".join(ciphertext)

# Función para imprimir la matriz de manera legible
def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))

# Función principal para ejecutar el Playfair Cipher
def playfair_cipher(key, plaintext):
    # Generar la matriz
    matriz = generar_matriz(key)
    
    # Cifrar el texto
    ciphertext = cifrar_playfair(plaintext, matriz)
    
    # Imprimir la matriz
    print("\nMatriz generada con la clave '{}':".format(key))
    imprimir_matriz(matriz)
    
    # Imprimir el texto plano y el ciphertext
    print("\nTexto plano: {}".format(plaintext))
    print("Ciphertext: {}".format(ciphertext))

# Ejemplo de uso
key = "MONARCHY"
plaintext = "BALLOON"
playfair_cipher(key, plaintext)
