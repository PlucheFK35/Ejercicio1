print("\n\t  Menu Principal.\n")

print(" 1. Celsius a Fahrenheit.\n 2. Segundos transcurridos.\n 3. Divisas.\n 4. Formula cuadratica.\n 5. Tipo de dato.\n 6. Salir. ")

try:
    opc = int(input("\nIngrese una opcion (1-5): "))
    if opc == 1:
        print("Celsius a Fahrenheit")

        celsius = float(input("Ingrese el valor en celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32

        print(celsius,"grados celsius es igual a",fahrenheit,"grados fahrenheit.") 
    if opc == 2:
        print("Segundos transcurridos.")

        hora = int(input("Ingrese la hora: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos_de_hora = (hora) * 3600
        segundos_de_minutos = (minutos) * 60
        segundos_totales = (segundos_de_hora) + (segundos_de_minutos)

        hora_actual = print(f"Su hora actual es: {hora}:{minutos}")
        print("Han pasado",segundos_totales,"segundos.")
    if opc == 3:
        print("Divisas (Dolares a quetzales)")

        dolares = float(input("Ingrese la cantidad en dolares: "))
        quetzales = (dolares) * 7.82

        result = print(f"${dolares} son Q.{quetzales}")
    if opc == 4:
        print("Ecuacion Cuadratica x^2+bx+c")

        a = int(input("ingrese el valor de a: "))
        b = int(input("ingrese el valor de b: "))
        c = int(input("ingrese el valor de c: "))

        discriminante = (b**2) - 4 * a * c
        x1 = (- b - (discriminante ** 0.5)) / 2 * a
        x2 = (- b + (discriminante ** 0.5)) / 2 * a

        print("el valor de x1 es:",x1)
        print("el valor de x2 es:",x2)
    if opc == 5:
        print("Tipo de DAto")

        dato = input("ingrese una variable: ")

        try:
            tipo = int(dato)
            variable = "Entero (int)"
        except ValueError:
            try:
                tipo = float(dato)
                variable = "Flotante (float)"
            except ValueError:
                variable = "Cadena (str)"
        
        print("La variable es de tipo:",variable)
    if opc == 6:
        print("Saliendo del programa...")

except:
    print("Opcion incorrecta...")

