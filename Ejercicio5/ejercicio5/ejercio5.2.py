from ejercicio import *


if __name__ == "__main__":
    lista = ListaEnlazada()

    print("--- Creación de la Lista Enlazada ---")
    while True:
        try:
            cantidad = int(input("¿Cuántos valores deseas añadir a la lista? "))
            if cantidad < 0:
                print("Por favor, ingresa un número no negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    for i in range(cantidad):
        while True:
            try:
                valor = input(f"Ingresa el valor #{i + 1}: ")
                # Intentamos convertir a int, si falla, lo dejamos como string
                # Puedes ajustar esto si solo quieres números o tipos específicos.
                try:
                    valor_procesado = int(valor)
                except ValueError:
                    valor_procesado = valor # Lo guardamos como string si no es número
                lista.agregar_valor(valor_procesado)
                break
            except Exception as e: # Captura general para otros posibles errores
                print(f"Ocurrió un error: {e}. Inténtalo de nuevo.")


    print("\n--- Lista Enlazada Creada ---")
    lista.mostrar_lista()

    print("\n--- Búsqueda en la Lista Enlazada ---")
    if not lista.cabeza:
        print("No se puede buscar en una lista vacía.")
    else:
        while True:
            valor_a_buscar = input("Ingresa el valor que deseas buscar (o escribe 'salir' para terminar): ")
            if valor_a_buscar.lower() == 'salir':
                break

            # Intentamos convertir a int si es posible, para coincidir con cómo se guardaron
            try:
                valor_procesado_busqueda = int(valor_a_buscar)
            except ValueError:
                valor_procesado_busqueda = valor_a_buscar

            resultado = lista.buscar_valor(valor_procesado_busqueda)
            print(resultado)

    print("\n¡Programa finalizado!")

