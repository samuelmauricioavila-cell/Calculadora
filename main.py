class Calculadora:
    def suma(self, a,b):
        return a+b
    def resta(self, a,b):
        return a-b
mi_calculadora = Calculadora() #objeto de la clase Calculadora
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
print("1. suma")
print("2. resta")
opcion=input("Seleccione una opción: ")
if opcion=="1":
    resultado=mi_calculadora.suma(num1,num2)
    print("El resultado de la suma es: ", resultado)
elif opcion=="2":
    resultado=mi_calculadora.resta(num1,num2)
    print("El resultado de la resta es: ", resultado)