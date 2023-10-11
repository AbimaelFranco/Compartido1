# Función para sumar dos números
def sumar(x, y):
    return x + y

# Función para restar dos números
def restar(x, y):
    return x - y

# Función para multiplicar dos números
def multiplicar(x, y):
    return x * y

# Función para dividir dos números
def dividir(x, y):
    if y == 0:
        return "No se puede dividir por cero."
    return x / y

# Menú de opciones
while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Solicitar al usuario que elija una opción
    opcion = input("Elija una opción (1/2/3/4/5): ")

    # Verificar si el usuario quiere salir
    if opcion == "5":
        print("¡Hasta luego!")
        break

    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación según la opción seleccionada
    if opcion == "1":
        print("Resultado:", sumar(num1, num2))

    elif opcion == "2":
        print("Resultado:", restar(num1, num2))

    elif opcion == "3":
        print("Resultado:", multiplicar(num1, num2))

    elif opcion == "4":
        print("Resultado:", dividir(num1, num2))

    else:
        print("Opción no válida")
