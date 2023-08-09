from modelo.vehiculo import Vehiculo
from modelo.punto import Punto
from modelo.rectangulo import Rectangulo
from modelo.circulo import Circulo
from modelo.carta import Carta

def menu():

    print("---------------------------------------")
    print("              Menu puntos              ")
    print("---------------------------------------")
    print("1. Punto #1")
    print("2. Puntos #2 y #3")
    print("3. Punto #4")
    print("4. Punto #5")
    print("5. Punto #6")
    print("6. Puntos #7, #8, #9, #10 y #11")
    print("7. Salir")
    print("---------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("---------------------------------------\n")

    return opcion

def opcion_1():

    vel_max = int(input("Ingrese la velocidad maxima del vehivulo: "))
    kilome = int(input("Ingrese el kilometraje del vehiculo: "))

    vehiculo = Vehiculo(velocidad_maxima = vel_max, kilometraje = kilome)

    print(f"La velocidad maxima del vehiculo ingresado es {vehiculo.velocidad_maxima} y su kilometraje es {vehiculo.kilometraje}")

    main()

def opcion_2():

    pnt_x = int(input("Ingrese el punto en el eje x (Entero): "))
    pnt_y = int(input("Ingrese el punto en el eje y (Entero): "))

    p1 = Punto(punto_x=pnt_x, punto_y=pnt_y)

    p1.mostrar_punto()

    cambiar = input("Desea cambiar las coordenadas(y/n): ")
    if cambiar == "y":
        pnt_x = int(input("Ingrese el punto en el eje x (Entero): "))
        pnt_y = int(input("Ingrese el punto en el eje y (Entero): "))
        p1.mover_punto(nuevo_punto_x=pnt_x, nuevo_punto_y=pnt_y)
    
    dist = input("Desea calcular la distancia entre dos puntos(y/n): ")
    if dist == "y":
        pnt_x_2 = int(input("Ingrese el punto en el eje x de la segunda coordenada (Entero): "))
        pnt_y_2 = int(input("Ingrese el punto en el eje y de la segunda coordenada (Entero): "))
        p2 = Punto(punto_x=pnt_x_2, punto_y=pnt_y_2)
        p2.mostrar_punto()
        distancia = p2.calcular_distancia(p1)
        print(f"La distancia entre el punto ({p1.punto_x},{p1.punto_y}) y el punto ({p2.punto_x},{p2.punto_y}) es de {round(distancia,4)}")

    main()

def opcion_3():

    print("----------------------------------")
    print("            Rectangulo            ")
    print("----------------------------------")
    pnt_x = int(input("Ingrese el punto en el eje x (Entero): "))
    pnt_y = int(input("Ingrese el punto en el eje y (Entero): "))

    p1 = Punto(punto_x=pnt_x, punto_y=pnt_y)

    p1.mostrar_punto()

    pnt_x = int(input("Ingrese el punto en el eje x de la segunda coordenada (Entero): "))
    pnt_y = int(input("Ingrese el punto en el eje y de la segunda coordenada (Entero): "))

    p2 = Punto(punto_x=pnt_x, punto_y=pnt_y)

    p2.mostrar_punto()

    bas = p1.calcular_base(p2)
    altur = p1.calcular_altura(p2)
    
    rect = Rectangulo(base=bas, altura=altur)
    peri = input("\nHallar perimetro(y/n): ")
    if peri == "y":
        rect.perimetro_rectangulo()
    are = input("\nHallar area(y/n): ")
    if are == "y":
        rect.area_rectangulo()
    es_rect = input("\nDesea saber si es rectangulo(y/n): ")
    if es_rect == "y":
        rect.es_rectangulo()

    main()
    
def opcion_4():

    print("----------------------------------")
    print("          Circunferencia          ")
    print("----------------------------------")
    pnt_x = int(input("Ingrese el punto del centro en el eje x (Entero): "))
    pnt_y = int(input("Ingrese el punto del centro en el eje y (Entero): "))

    cen = Punto(punto_x=pnt_x, punto_y=pnt_y)

    cen.mostrar_punto()
    rad = float(input("Ingrese el radio de la circunferencia: "))
    circu = Circulo(radio=rad, centro=cen)
    peri = input("\nHallar perimetro(y/n): ")
    if peri == "y":
        circu.perimetro_circunferecia()
    are = input("\nHallar area(y/n): ")
    if are == "y":
        circu.area_circunferencia()
    es_rect = input("\nDesea saber si un punto se encuentra dentro de la circunferencia(y/n): ")
    if es_rect == "y":
        pnt_x = int(input("Ingrese el punto en el eje x (Entero): "))
        pnt_y = int(input("Ingrese el punto en el eje y (Entero): "))
        p2 = Punto(punto_x=pnt_x, punto_y=pnt_y)
        p2.mostrar_punto()
        distancia = p2.calcular_distancia(cen)
        if distancia > rad:
            print(f"El punto ({p2.punto_x},{p2.punto_y}) no hace parte de la circunferencia ya que la distancia al centro es {round(distancia,4)} la cual es mayor al radio {rad}")
        else:
            print(f"El punto ({p2.punto_x},{p2.punto_y}) hace parte de la circunferencia ya que la distancia al centro es {round(distancia,4)} la cual es menor/igual al radio {rad}")

    main()

def opcion_5():

    print("----------------------------------")
    print("               Carta              ")
    print("----------------------------------\n")
    print("Tipo de valor")
    print("1. Numero\n2. Letra")
    tipo_valor = int(input("Ingrese el tipo de valor que deseas ingresar: "))
    if tipo_valor == 1:
        valorN = int(input("Ingrese el valor de la carta (2-10): "))
        print("\nPintas:")
        print("1. Diamante\n2. Trebol\n3. Corazon\n4. Pica")
        pinta = int(input("Ingrese el numero que corresponde a la pinta de la carta: "))
        if pinta == 1:
            carta = Carta(valor=valorN, pinta=Carta.PINTA_DIAMANTE)
        if pinta == 2:
            carta = Carta(valor=valorN, pinta=Carta.PINTA_TREBOL)
        if pinta == 3:
            carta = Carta(valor=valorN, pinta=Carta.PINTA_CORAZON)
        if pinta == 4:
            carta = Carta(valor=valorN, pinta=Carta.PINTA_PICA)
        print(f"\nSu carta es un {carta.valor} de {carta.pinta}\n")
    elif tipo_valor == 2:
        valorL = input("Ingrese el valor de la carta (A, J, Q, K): ")
        print("\nPintas:")
        print("1. Diamante\n2. Trebol\n3. Corazon\n4. Pica")
        pinta = int(input("Ingrese el numero que corresponde a la pinta de la carta: "))
        if pinta == 1:
            carta = Carta(valor=valorL, pinta=Carta.PINTA_DIAMANTE)
        if pinta == 2:
            carta = Carta(valor=valorL, pinta=Carta.PINTA_TREBOL)
        if pinta == 3:
            carta = Carta(valor=valorL, pinta=Carta.PINTA_CORAZON)
        if pinta == 4:
            carta = Carta(valor=valorL, pinta=Carta.PINTA_PICA)
        print(f"\nSu carta es un {carta.valor} de {carta.pinta}\n")
    else:
        print("Opcion no valida.")

    main()

def opcion_6():


    return

def main():

    opcion = menu()
    if opcion == 1:
        opcion_1()
    if opcion == 2:
        opcion_2()
    if opcion == 3:
        opcion_3()
    if opcion == 4:
        opcion_4()
    if opcion == 5:
        opcion_5()
    if opcion == 6:
        opcion_6()

main() 