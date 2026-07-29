from operaciones_basicas import OperacionesBasicas
calc_basica=OperacionesBasicas()
acumulativo=False
while True:
    if acumulativo:
        calc_basica.num1=calc_basica.resultado
    else:
        calc_basica.num1=float(input("Ingrese el primer número: "))
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Limpiar")
    print("6. Salir")
    opcion=input("Seleccione una opción: ")
