from funciones_pila import invertir_frase

def main():
    frase = "Hola mundo desde UAM"
    resultado = invertir_frase(frase)
    print("Frase original: ", frase)
    print("Frase invertida:", resultado)

if __name__ == "__main__":
    main()