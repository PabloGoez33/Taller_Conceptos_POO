class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro_rectangulo(self):
        perimetro = (2 * self.base) + (2 * self.altura)
        print(f"El perimetro del rectangulo es {perimetro}.")
    
    def area_rectangulo(self):
        area = self.base * self.altura
        print(f"El area del rectangulo es {area}.")
    
    def es_rectangulo(self):
        if self.base == self.altura:
            print("No es rectangulo, es cuadrado.")
        else:
            print("Es rectangulo.")
        return