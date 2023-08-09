class Punto:

    def __init__(self,punto_x, punto_y) :
        self.punto_x = punto_x
        self.punto_y = punto_y

    def mostrar_punto(self):
        print(f"Las coordenadas que ingresaste (X,Y) son: ({self.punto_x},{self.punto_y})")

    def mover_punto(self, nuevo_punto_x, nuevo_punto_y):
        self.punto_x = nuevo_punto_x
        self.punto_y = nuevo_punto_y
        print(f"Las nuevas coordenadas (X,Y) son: ({self.punto_x},{self.punto_y})")

    def calcular_distancia(self, punto):
        distancia = (((punto.punto_x - self.punto_x) ** 2)+((punto.punto_y - self.punto_y) ** 2)) ** 0.5
        return distancia

    def calcular_base(self, punto):
        base = (punto.punto_x - self.punto_x)
        return base

    def calcular_altura(self, punto):
        altura = (punto.punto_y - self.punto_y)
        return altura