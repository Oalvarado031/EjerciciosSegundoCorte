
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.actual = None

    def agregar_cancion(self, nombre):
        nuevo = NodoCancion(nombre)
        if not self.primero:
            self.primero = nuevo
            self.actual = nuevo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp

    def eliminar_cancion(self, nombre):
        temp = self.primero
        while temp:
            if temp.nombre == nombre:
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primero = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior
                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior
                print(f"Canción '{nombre}' eliminada.")
                return
            temp = temp.siguiente
        print(f"Canción '{nombre}' no encontrada.")

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print(f"Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay siguiente canción.")

    def anterior_cancion(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print(f"Reproduciendo: {self.actual.nombre}")
        else:
            print("No hay canción anterior.")

    def mostrar_lista(self):
        temp = self.primero
        print("Lista de reproducción:")
        while temp:
            if temp == self.actual:
                print(f"-> {temp.nombre} (reproduciendo)")
            else:
                print(f"   {temp.nombre}")
            temp = temp.siguiente
