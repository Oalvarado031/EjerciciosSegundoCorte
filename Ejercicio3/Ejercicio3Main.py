# main.py

from Ejercicio3Funciones import ListaReproduccion

def menu():
    reproductor = ListaReproduccion()
    while True:
        print("\n1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente")
        print("4. Reproducir anterior")
        print("5. Mostrar lista")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la canción: ")
            reproductor.agregar_cancion(nombre)
        elif opcion == "2":
            nombre = input("Nombre de la canción a eliminar: ")
            reproductor.eliminar_cancion(nombre)
        elif opcion == "3":
            reproductor.siguiente_cancion()
        elif opcion == "4":
            reproductor.anterior_cancion()
        elif opcion == "5":
            reproductor.mostrar_lista()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
