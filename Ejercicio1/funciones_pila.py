def invertir_frase(frase):
    palabras = frase.split() # Dividir la frase en palabras usando espacios como separador
    pila = [None] * len(palabras)  # Pila con tamaño fijo
    tope = 0 # Apunta a la posición disponible para insertar

    # Insertar palabras
    for i in range(len(palabras)):
        pila[tope] = palabras[i]
        tope += 1

# Sacar las palabras de la pila en orden inverso
    frase_invertida = ""
    while tope > 0:
        tope -= 1
        frase_invertida += pila[tope] + " "

    return frase_invertida.strip()