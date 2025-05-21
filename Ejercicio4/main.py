from funciones_cola import ColaDePrioridad

def main():
    # Crear una cola con capacidad para 5 elementos
    cola = ColaDePrioridad(5)

    # Insertar elementos en la cola
    cola.encolar("Tarea A", 3)
    cola.encolar("Tarea B", 1)
    cola.encolar("Tarea C", 2)

    # Mostrar el estado actual de la cola
    cola.mostrar()

    # Desencolar los elementos por orden de prioridad (menor número sale primero)
    print("\nDesencolando por prioridad:")
    print("Atendiendo:", cola.desencolar())
    print("Atendiendo:", cola.desencolar())

    # Mostrar la cola después de desencolar algunos elementos
    cola.mostrar()

# Punto de entrada del programa
if __name__ == "__main__":
    main()