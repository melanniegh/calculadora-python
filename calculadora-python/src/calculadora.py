def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(a, b):
    return a ** b

def main():
    print("Calculadora simple en Python")
    print("Operaciones disponibles: suma, resta, multiplicación, división, potencia")

    while True:
        op = input("\nEscribe la operación (suma/resta/multiplicación/división/potencia) o 'salir' para terminar: ").lower()
        if op == "salir":
            break
        if op not in ["suma", "resta", "multiplicación", "division", "potencia", "división"]:
            print("Operación no válida.")
            continue
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        if op == "suma":
            print("Resultado:", sumar(a, b))
        elif op == "resta":
            print("Resultado:", restar(a, b))
        elif op == "multiplicación":
            print("Resultado:", multiplicar(a, b))
        elif op in ["división", "division"]:
            print("Resultado:", dividir(a, b))
        elif op == "potencia":
            print("Resultado:", potencia(a, b))

if __name__ == "__main__":
    main()
