# Clase que representa un nodo de la lista (una canción)
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre          # Nombre de la canción
        self.siguiente = None         # Enlace al siguiente nodo
        self.anterior = None          # Enlace al nodo anterior

# Clase que representa la lista de reproducción
class ListaReproduccion:
    def __init__(self):
        self.primero = None           # Primer nodo de la lista
        self.actual = None            # Nodo actualmente en reproducción

    # Agrega una canción al final de la lista
    def agregar_cancion(self, nombre):
        nuevo = NodoCancion(nombre)
        if not self.primero:          # Si la lista está vacía
            self.primero = nuevo
            self.actual = nuevo
        else:
            temp = self.primero
            while temp.siguiente:     # Recorre hasta el último nodo
                temp = temp.siguiente
            temp.siguiente = nuevo    # Conecta el nuevo nodo al final
            nuevo.anterior = temp     # Enlace hacia atrás

    # Elimina una canción por nombre
    def eliminar_cancion(self, nombre):
        temp = self.primero
        while temp:
            if temp.nombre == nombre:
                # Ajusta enlaces del nodo anterior y siguiente
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primero = temp.siguiente  # Eliminando el primero

                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior

                # Si se elimina la canción actual, mueve el puntero actual
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior

                print(f"Canción '{nombre}' eliminada.")
                return
            temp = temp.siguiente

        print(f"Canción '{nombre}' no encontrada.")

    # Reproduce la siguiente canción en la lista
    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay siguiente canción.")

    # Reproduce la canción anterior
    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay canción anterior.")

    # Muestra toda la lista de reproducción
    def mostrar_lista(self):
        temp = self.primero
        print("Lista de reproducción:")
        while temp:
            # Indica cuál es la canción que está siendo reproducida
            if temp == self.actual:
                print(f"-> {temp.nombre} (reproduciendo)")
            else:
                print(f"   {temp.nombre}")
            temp = temp.siguiente

