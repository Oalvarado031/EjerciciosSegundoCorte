'''Ejercicio #5: Búsqueda en una lista enlazada. 
Cree una función que busque un valor específico en una lista enlazada. 
La función debe devolver la posición del valor si se encuentra, o un mensaje indicando 
que el valor no está en la lista.'''

class Nodo:
    """
    Clase para representar un nodo en la lista enlazada.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    """
    Clase para representar una lista enlazada.
    """
    def __init__(self):
        self.cabeza = None

    def agregar_valor(self, dato):
        """
        Agrega un nuevo nodo con el dato proporcionado al final de la lista.
        """
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar_valor(self, valor_buscado):
        """
        Busca un valor específico en la lista enlazada.

        Args:
            valor_buscado: El valor a buscar en la lista.

        Returns:
            La posición (índice basado en 0) del valor si se encuentra.
            Un mensaje indicando que el valor no está en la lista si no se encuentra.
        """
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == valor_buscado:
                return f"El valor {valor_buscado} se encuentra en la posición {posicion}."
            actual = actual.siguiente
            posicion += 1
        return f"El valor {valor_buscado} no se encuentra en la lista."

    def mostrar_lista(self):
        """
        Muestra los elementos de la lista enlazada.
        """
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        if not elementos:
            print("La lista está vacía.")
        else:
            print(" -> ".join(elementos))

