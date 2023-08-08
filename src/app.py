from modelo.vehiculo import Vehiculo
from modelo.punto import Punto
from modelo.rectangulo import Rectangulo

def menu():

    print("---------------------------------------")
    print("              Menu puntos              ")
    print("---------------------------------------")
    print("1. Punto #1")
    print("2. Puntos #2 y #3")
    print("3. Punto #4")
    print("4. Punto #1")
    print("5. Punto #1")
    print("6. Punto #1")
    print("7. Salir")
    print("---------------------------------------")
    opcion = int(input("Ingrese la opcion: "))
    print("---------------------------------------")

    return opcion

def punto_1():

    vel_max = int(input("Ingrese la velocidad maxima del vehivulo: "))
    kilome = int(input("Ingrese el kilometraje del vehiculo: "))

    vehiculo = Vehiculo(velocidad_maxima = vel_max, kilometraje = kilome)

    print(f"La velocidad maxima del vehiculo ingresado es {vehiculo.velocidad_maxima} y su kilometraje es {vehiculo.kilometraje}")

    main()

def punto_2():

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
        pnt_x_2 = int(input("Ingrese el punto en el eje x (Entero): "))
        pnt_y_2 = int(input("Ingrese el punto en el eje y (Entero): "))
        p2 = Punto(punto_x=pnt_x_2, punto_y=pnt_y_2)
        p2.mostrar_punto()
        Punto.calcular_distancia(pnt_x, pnt_y, pnt_x_2, pnt_y_2)

    main()

def punto_3():

    print("Ingrese los puntos de las esquinas del cuadrilatero, \nrecuerda empezar desde la esquina superior izquierda e irlos \ningresando  en sentido de las manecillas del rolej.")
    print("\n--------Ingrese punto esquina #1--------")
    pnt_x_1 = int(input("Ingrese el punto en el eje x de la esquina 1 (Entero): "))
    pnt_y_1 = int(input("Ingrese el punto en el eje y de la esquina 1 (Entero): "))
    print("\n--------Ingrese punto esquina #2--------")
    pnt_x_2 = int(input("Ingrese el punto en el eje x de la esquina 2 (Entero): "))
    pnt_y_2 = int(input("Ingrese el punto en el eje y de la esquina 2 (Entero): "))
    print("\n--------Ingrese punto esquina #3--------")
    pnt_x_3 = int(input("Ingrese el punto en el eje x de la esquina 3 (Entero): "))
    pnt_y_3 = int(input("Ingrese el punto en el eje y de la esquina 3 (Entero): "))
    print("\n--------Ingrese punto esquina #4--------")
    pnt_x_4 = int(input("Ingrese el punto en el eje x de la esquina 4 (Entero): "))
    pnt_y_4 = int(input("Ingrese el punto en el eje y de la esquina 4 (Entero): "))

    Rectangulo.calcular_distancia(punto_x_1=pnt_x_1, punto_y_1=pnt_y_1, punto_x_2=pnt_x_2, punto_y_2=pnt_y_2, punto_x_3=pnt_x_3, punto_y_3=pnt_y_3, punto_x_4=pnt_x_4,punto_y_4=pnt_y_4)

    

def punto_4():


    return

def punto_5():


    return

def punto_6():


    return

def main():

    opcion = menu()
    if opcion == 1:
        punto_1()
    if opcion == 2:
        punto_2()
    if opcion == 3:
        punto_3()
    if opcion == 4:
        punto_4()
    if opcion == 5:
        punto_5()
    if opcion == 6:
        punto_6()

main() 