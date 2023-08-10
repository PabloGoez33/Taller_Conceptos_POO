class CuentaBancaria:

    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def mostrar_detalles(self):
        print(f"\nCuenta N°: {self.numero_cuenta}")
        print(f"Propietario: {self.propietario}")
        print(f"Balance: {self.balance}")
    
    def depositar(self, cantidad, cuenta_depo):
        balance_anterior = self.balance
        if cuenta_depo == self.numero_cuenta:
            self.balance = self.balance + cantidad
            print("\nDeposito realizado")
            print(f"Al numero de cuenta: {cuenta_depo}")
            print(f"Monto del deposito: {cantidad}")
            print(f"Balance anterior: {balance_anterior}")
            print(f"Balance actual: {self.balance}")
        else:
            print("Lo sentimos ceunta incorrecta.")
    
    def retirar(self, cantidad, cuenta_reti):
        balance_anterior = self.balance
        if cuenta_reti == self.numero_cuenta:
            if cantidad < self.balance:
                self.balance = self.balance - cantidad
                print("\nRetiro realizado")
                print(f"Se retiro del numero de cuenta: {cuenta_reti}")
                print(f"El total de: {cantidad}")
                print(f"Balance anterior: {balance_anterior}")
                print(f"Balance actual: {self.balance}")
            else:
                print("El monto a retirar supera la cantidad de dinero disponible.")
        else:
            print("Lo lamento cuenta incorrecta y/o no encontrada.")

    def aplicar_cuota_manejo(self):
        self.balance = self.balance - ((2 / 100) * self.balance)
        print(f"Su cuenta luego de aplicar la cuota de manejo quedo en {self.balance}")