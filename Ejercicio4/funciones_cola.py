# Clase que representa un elemento de la cola con nombre y prioridad
class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre              # Nombre del elemento (por ejemplo, "Tarea A")
        self.prioridad = prioridad        # Prioridad numérica (menor número = mayor prioridad)

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"


# Clase que representa la cola de prioridad
class ColaDePrioridad:
    def __init__(self, capacidad):
        self.cola = [None] * capacidad    # Arreglo fijo que almacena los elementos
        self.tamano = 0                   # Cantidad actual de elementos en la cola
        self.capacidad = capacidad        # Capacidad máxima de la cola

    # Método para insertar un nuevo elemento en la cola
    def encolar(self, nombre, prioridad):
        if self.tamano >= self.capacidad:
            print("Cola llena. No se puede encolar.")
            return
        
        # Crear el nuevo elemento y colocarlo en la posición disponible
        nuevo = Elemento(nombre, prioridad)
        self.cola[self.tamano] = nuevo
        self.tamano += 1  # Aumentar el tamaño de la cola

    # Método para eliminar el elemento con mayor prioridad (menor número)
    def desencolar(self):
        if self.tamano == 0:
            print("Cola vacía.")
            return None

        # Buscar el índice del elemento con menor prioridad numérica
        indice = 0
        for i in range(1, self.tamano):
            if self.cola[i].prioridad < self.cola[indice].prioridad:
                indice = i

        # Guardar el elemento que se va a retirar
        elemento = self.cola[indice]

        # Mover los elementos restantes para llenar el hueco
        for j in range(indice, self.tamano - 1):
            self.cola[j] = self.cola[j + 1]

        # Limpiar la última posición
        self.cola[self.tamano - 1] = None
        self.tamano -= 1  # Reducir tamaño de la cola

        return elemento

    # Método para mostrar el contenido actual de la cola
    def mostrar(self):
        if self.tamano == 0:
            print("La cola está vacía.")
        else:
            print("Elementos en la cola:")
            for i in range(self.tamano):
                print(" -", self.cola[i])