def invertir_frase(frase):
    palabras = frase.split()
    pila = [None] * len(palabras)  # Pila con tamaño fijo
    tope = 0

    # Insertar palabras
    for i in range(len(palabras)):
        pila[tope] = palabras[i]
        tope += 1

    frase_invertida = ""
    while tope > 0:
        tope -= 1
        frase_invertida += pila[tope] + " "

    return frase_invertida.strip()