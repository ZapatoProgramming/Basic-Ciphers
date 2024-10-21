from collections import Counter

def frecuencias_relativas(ciphertext):
    # Contar las ocurrencias de cada símbolo en el ciphertext
    conteos = Counter(ciphertext)
    
    # Calcular la longitud total del ciphertext
    total_simbolos = len(ciphertext)
    
    # Calcular las frecuencias relativas en porcentaje
    frecuencias_relativas = {simbolo: (conteo / total_simbolos) * 100 for simbolo, conteo in conteos.items()}
    
    return frecuencias_relativas

def imprimir_frecuencias_bonito(frecuencias):
    print("Símbolo\tFrecuencia (%)")
    print("-" * 30)
    
    # Ordenar las frecuencias de mayor a menor
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)
    
    for simbolo, frecuencia in frecuencias_ordenadas:
        # Usamos repr para mostrar los símbolos no imprimibles y format para formatear el porcentaje
        print(f"{repr(simbolo)}\t{frecuencia:.2f}")

# Texto cifrado
ciphertext = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
frecuencias = frecuencias_relativas(ciphertext)
imprimir_frecuencias_bonito(frecuencias)
