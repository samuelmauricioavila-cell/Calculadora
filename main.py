from operaciones_basicas import OperacionesBasicas
calc_basica=OperacionesBasicas()
acumulativo=False
while True:
    if acumulativo:
        print(f"Número actual: {calc_basica.num1}")
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
    if opcion=="6":
        print ("Saliendo del programa...")
        break
    elif opcion=="5":
        acumulativo=False
        print("Se ha limpiado el acumulativo.")
        continue
    if opcion in ["1", "2", "3", "4"]:
        calc_basica.num2=float(input("Ingrese el segundo número: "))
    if opcion=="1":
        res=calc_basica.suma()
    elif opcion=="2":
        res=calc_basica.resta()
    elif opcion=="3":
        res=calc_basica.multiplicacion()
    elif opcion=="4":
        res=calc_basica.division()
    else:
        print("Opción inválida. ")
        continue
    print(f"-> Resultado: {res}")
    if isinstance(res, (int, float)):
        acumulativo=True
    else: 
        acumulativo=False



