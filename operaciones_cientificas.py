import math

class OperacionesCientificas:
    def __init__(self):
        self.base = 0.0
        self.exponente = 0.0
        self.radicando = 0.0
        self.indice = 0.0
        self.angulo = 0.0
        self.resultado = 0.0

    def pedir_potencia(self):
        self.base = float(input("Ingrese la base: "))
        self.exponente = float(input("Ingrese el exponente: "))

    def pedir_raiz(self):
        self.radicando = float(input("Ingrese el radicando: "))
        self.indice = float(input("Ingrese el índice: "))

    def pedir_angulo(self):
        self.angulo = float(input("Ingrese el ángulo en grados: "))  

    def potencia_enesima(self):
        self.pedir_potencia()
        if self.base == 0 and self.exponente < 0:
            print("Error: No se puede calcular la potencia de 0 con exponente negativo.")
            return None
        self.resultado = self.base ** self.exponente
        print(f"-> Resultado: {self.base} ^ {self.exponente} = {self.resultado}")
        return self.resultado

    def raiz_enesima(self):
        self.pedir_raiz()
        if self.indice == 0:
            print("Error: No se puede calcular la raíz enésima con índice 0.")
            return None  # Se agrega return para evitar ZeroDivisionError
            
        if self.radicando < 0 and self.indice % 2 == 0:
            print("Error: Operación inválida. Genera un resultado complejo.")
            return None
            
        if self.radicando < 0:
            self.resultado = -((-self.radicando) ** (1 / self.indice))
        else:
            self.resultado = self.radicando ** (1 / self.indice)
            
        print(f"-> Resultado: Raíz {self.indice} de {self.radicando} = {self.resultado}")
        return self.resultado

    def seno(self):
        self.pedir_angulo()
        radianes = math.radians(self.angulo)
        self.resultado = math.sin(radianes)
        print(f"sen({self.angulo}°) = {round(self.resultado, 6)}")
        return self.resultado

    def coseno(self):
        self.pedir_angulo()
        radianes = math.radians(self.angulo)
        self.resultado = math.cos(radianes)
        print(f"cos({self.angulo}°) = {round(self.resultado, 6)}")
        return self.resultado

    def tangente(self):
        self.pedir_angulo()
        if (self.angulo % 180) == 90:
            print(f"Error: La tangente de {self.angulo}° no está definida (división entre cero).")
            return None
            
        radianes = math.radians(self.angulo)
        self.resultado = math.tan(radianes)
        print(f"tan({self.angulo}°) = {round(self.resultado, 6)}")
        return self.resultado