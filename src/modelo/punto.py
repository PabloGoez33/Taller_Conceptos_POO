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

    def calcular_distancia(punto_x_1, punto_y_1, punto_x_2, punto_y_2):
        distancia = (((punto_x_2 - punto_x_1) ** 2)+((punto_y_2 - punto_y_1) ** 2)) ** 0.5
        print(f"La distancia entre el punto ({punto_x_1},{punto_y_1}) y el punto ({punto_x_2},{punto_y_2}) es de {round(distancia,4)}")