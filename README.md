class calculadora:
    def suma(self, a,b):
        return a+b
    def resta(self, a,b):
        return a-b
    def multiplicacion(self, a,b):
        return a*b
    def division(self, a,b):
        return a/b
micalc= calculadora() #objeto
num1=float(input("ingrese el primer numero: "))
num2=float(input("ingrese el segundo numero: "))

print("1, suma")
print("2, resta")

opcion=input("seleccione una opcion: ")

if opcion=="1":
    resultado=micalc.suma(num1,num2)
    print("resultado de la suma: ", resultado)

elif opcion=="2":
    resultado=micalc.resta(num1,num2)
    print("resultado de la resta: ", resultado)
else:
    print("opcion invalida")
