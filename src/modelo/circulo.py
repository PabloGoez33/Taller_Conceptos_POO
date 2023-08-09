class Circulo:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def perimetro_circunferecia(self):
        perimetro = 2 * 3.1416 * self.radio
        print(f"El perimetro de la circunferencia es {perimetro}.")
    
    def area_circunferencia(self):
        area = 3.1416 * (self.radio ** 2)
        print(f"El area de la circunferencia es {area}.")