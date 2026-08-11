from operaciones_basicas import OperacionesBasicas
from operaciones_cientificas import OperacionesCientificas
from operaciones_especiales import OperacionesEspeciales

def ejecutar_calculadora():
    # Instanciación de los objetos (requerido por la guía)[cite: 1]
    calc_basica = OperacionesBasicas()
    calc_cientifica = OperacionesCientificas()
    calc_especial = OperacionesEspeciales()

    acumulativo = False
    
    while True:
        print("          CALCULADORA MULTIFUNCIONAL       ")

        if acumulativo:
            print(f"-> Número acumulado actual: {calc_basica.num1}")
        
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia enésima")
        print("6. Raíz enésima")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Factorial")
        print("11. Serie de Fibonacci")
        print("12. Máximo Común Divisor (MCD)")
        print("13. Mínimo Común Múltiplo (MCM)")
        print("14. Calcular IVA")
        print("15. Limpiar número acumulado")
        print("16. Salir")
        print("- - - - - - - - - - - - - - - - - - - - -")

        opcion = input("Seleccione una opción: ")

        if opcion == "16":
            print("Saliendo del programa... ¡Hasta luego!")
            break
            
        elif opcion == "15":
            acumulativo = False
            calc_basica.num1 = 0.0
            print("Se ha limpiado el valor acumulado.")
            continue

        if opcion in ["1", "2", "3", "4"]:
            if not acumulativo:
                calc_basica.num1 = float(input("Ingrese el primer número: "))
            
            calc_basica.num2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                res = calc_basica.suma()
            elif opcion == "2":
                res = calc_basica.resta()
            elif opcion == "3":
                res = calc_basica.multiplicacion()
            elif opcion == "4":
                res = calc_basica.division()

            print(f"-> Resultado: {res}")

            if isinstance(res, (int, float)):
                calc_basica.num1 = res
                acumulativo = True
            else:
                acumulativo = False

        elif opcion in ["5", "6", "7", "8", "9"]:
            res = None
            if opcion == "5":
                res = calc_cientifica.potencia_enesima()
            elif opcion == "6":
                res = calc_cientifica.raiz_enesima()
            elif opcion == "7":
                res = calc_cientifica.seno()
            elif opcion == "8":
                res = calc_cientifica.coseno()
            elif opcion == "9":
                res = calc_cientifica.tangente()

            if res is not None:
                calc_basica.num1 = res
                acumulativo = True
            else:
                acumulativo = False

        elif opcion in ["10", "11", "12", "13", "14"]:
            res = None
            if opcion == "10":
                res = calc_especial.factorial()
            elif opcion == "11":
                res = calc_especial.fibonacci()
            elif opcion == "12":
                res = calc_especial.maximo_comun_divisor()
            elif opcion == "13":
                res = calc_especial.minimo_comun_multiplo()
            elif opcion == "14":
                res = calc_especial.calcular_iva()

            if res is not None:
                calc_basica.num1 = res
                acumulativo = True
            else:
                acumulativo = False

        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_calculadora()