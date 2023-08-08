from modelo.vehiculo import Vehiculo
from modelo.punto import Punto

def menu():

    print("---------------------------------------")
    print("              Menu puntos              ")
    print("---------------------------------------")
    print("1. Punto #1")
    print("2. Puntos #2 y #3")
    print("3. Punto #1")
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


    return

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