def verificar_parentesis_balanceados(cadena):
    pila = []  # Se usa una lista como pila
    pares = {')': '(', '}': '{', ']': '['}  # Diccionario para verificar correspondencia

    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)  # Se Agrega paréntesis de apertura a la pila
        elif caracter in ')}]':
            if not pila:
                return False  # Si hay un cierre pero la pila está vacía, está desbalanceado
            if pila[-1] == pares[caracter]:
                pila.pop()  # Quita el par que hace match
            else:
                return False  # No hay coincidencia entre apertura y cierre

    return len(pila) == 0  # Si la pila está vacía, todo está balanceado

# Pruebas
texto = input("Ingresa una cadena para verificar los paréntesis: ")
if verificar_parentesis_balanceados(texto):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis NO están balanceados.")
