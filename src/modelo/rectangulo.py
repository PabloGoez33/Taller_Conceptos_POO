class Rectangulo:

    def __init__(self, punto_x, punto_y):
        self.punto_x = punto_x
        self.punto_y = punto_y
    
    def calcular_distancia(punto_x_1, punto_y_1, punto_x_2, punto_y_2, punto_x_3, punto_y_3, punto_x_4, punto_y_4):
        distancia_1_2 = (((punto_x_2 - punto_x_1) ** 2)+((punto_y_2 - punto_y_1) ** 2)) ** 0.5
        print(f"La distancia entre el punto ({punto_x_1},{punto_y_1}) y el punto ({punto_x_2},{punto_y_2}) es de {round(distancia_1_2,4)}")
        distancia_2_3 = (((punto_x_3 - punto_x_2) ** 2)+((punto_y_3 - punto_y_2) ** 2)) ** 0.5
        print(f"La distancia entre el punto ({punto_x_2},{punto_y_2}) y el punto ({punto_x_3},{punto_y_3}) es de {round(distancia_2_3,4)}")
        distancia_3_4 = (((punto_x_4 - punto_x_3) ** 2)+((punto_y_4 - punto_y_3) ** 2)) ** 0.5
        print(f"La distancia entre el punto ({punto_x_3},{punto_y_3}) y el punto ({punto_x_4},{punto_y_4}) es de {round(distancia_3_4,4)}")
        distancia_4_1 = (((punto_x_1 - punto_x_4) ** 2)+((punto_y_1 - punto_y_4) ** 2)) ** 0.5
        print(f"La distancia entre el punto ({punto_x_4},{punto_y_4}) y el punto ({punto_x_1},{punto_y_1}) es de {round(distancia_4_1,4)}")

        return 

    def validar_rectangulo():
        return