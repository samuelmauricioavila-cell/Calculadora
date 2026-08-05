import math

class OperacionesCientificas:
    def __init__(self):
        self.base = 0.0
        self.exponente = 0.0
        self.radicando = 0.0
        self.indice = 0.0
        self.angulo = 0.0
        self.resultado = 0.0
    def potencia(self):
        self.base = float(input("Ingrese la base:"))
        self.exponente = float(input("Ingrese el exponente:"))
    def raiz(self):
        self.radicando = float(input("Ingrese el radicando:"))
        self.indice = float(input("Ingrese el índice:"))
    def angulo(self):
        self.angulo = float(input("Ingrese el angulo en grados:"))  
    def potencia_enesima(self):
        self.potencia()
        if self.base == 0 and self.exponente < 0:
            print("Error: No se puede calcular la potencia de 0 con exponente negativo.")
            return
        self.resultado = self.base ** self.exponente
        print(f"-> Resultado: {self.base} ^ {self.exponente} = {self.resultado}")
    def raiz_enesima(self):
        self.raiz()
        if self.indice == 0:
            print("Error: No se puede calcular la raíz enésima con indice 0.")
        if self.radicando < 0 and self.indice % 2 == 0:
            print("Error: Operacion invalida. Genera un resultado complejo.")
            return
        if self.radicando < 0:
            self.resultado = -((-self.radicando) ** (1 / self.indice))
        else:
            self.resultado = self.radicando ** (1/self.indice)
            print(f"-> Resultado: Raiz {self.indice} de {self.radicando} = {self.resultado}")
    def seno(self):
        self.angulo()
        radianes = math.radians(self.angulo)
        self.resultado = math.sin(radianes)
        print(f"sen({self.angulo}°) = {round(self.resultado, 6)}")