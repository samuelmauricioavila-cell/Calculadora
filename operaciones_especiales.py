class OperacionesEspeciales:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.monto = 0.0
        self.porcentaje_iva = 0.0
        self.resultado = 0.0

    def pedir_un_numero(self):
        self.num1 = int(input("Ingrese el número entero (n): "))

    def pedir_dos_numeros(self):
        self.num1 = int(input("Ingrese el primer número entero: "))
        self.num2 = int(input("Ingrese el segundo número entero: "))

    def pedir_datos_iva(self):
        self.monto = float(input("Ingrese el valor o monto base: "))
        self.porcentaje_iva = float(input("Ingrese el porcentaje de IVA (%): "))

    def factorial(self):
        self.pedir_un_numero()
        if self.num1 < 0:
            print("Error: No existe el factorial de un número negativo.")
            return None
        
        fact = 1
        for i in range(1, self.num1 + 1):
            fact *= i
            
        self.resultado = fact
        print(f"-> Resultado: {self.num1}! = {self.resultado}")
        return self.resultado

    def fibonacci(self):
        self.pedir_un_numero()
        if self.num1 <= 0:
            print("Error: La posición en la serie de Fibonacci debe ser mayor a 0.")
            return None
        
        if self.num1 == 1:
            self.resultado = 0
        elif self.num1 == 2:
            self.resultado = 1
        else:
            a, b = 0, 1
            for _ in range(3, self.num1 + 1):
                a, b = b, a + b
            self.resultado = b
            
        print(f"-> Resultado: El número en la posición {self.num1} de Fibonacci es: {self.resultado}")
        return self.resultado

    def maximo_comun_divisor(self):
        self.pedir_dos_numeros()
        a = abs(self.num1)
        b = abs(self.num2)
        
        if a == 0 and b == 0:
            print("Error: El MCD de 0 y 0 no está definido.")
            return None
            
        while b != 0:
            a, b = b, a % b
            
        self.resultado = a
        print(f"-> Resultado: MCD({self.num1}, {self.num2}) = {self.resultado}")
        return self.resultado

    def minimo_comun_multiplo(self):
        self.pedir_dos_numeros()
        if self.num1 == 0 or self.num2 == 0:
            self.resultado = 0
            print(f"-> Resultado: MCM({self.num1}, {self.num2}) = {self.resultado}")
            return self.resultado

        a = abs(self.num1)
        b = abs(self.num2)
        temp_a, temp_b = a, b
        
        while temp_b != 0:
            temp_a, temp_b = temp_b, temp_a % temp_b
        
        mcd = temp_a
        self.resultado = (a * b) // mcd
        print(f"-> Resultado: MCM({self.num1}, {self.num2}) = {self.resultado}")
        return self.resultado

    def calcular_iva(self):
        self.pedir_datos_iva()
        if self.monto < 0 or self.porcentaje_iva < 0:
            print("Error: El monto y el porcentaje deben ser positivos.")
            return None

        valor_iva = self.monto * (self.porcentaje_iva / 100)
        total = self.monto + valor_iva
        self.resultado = total
        
        print(f"-> Valor del IVA ({self.porcentaje_iva}%): ${valor_iva:.2f}")
        print(f"-> Total con IVA incluido: ${total:.2f}")
        return self.resultado
    



