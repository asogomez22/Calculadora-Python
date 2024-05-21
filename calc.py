import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

print("Calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potenciación")
print("6. Raíz cuadrada")
print("7. Seno")
print("8. Coseno")
print("9. Tangente")

opcion = input("Elige una operación (1/2/3/4/5/6/7/8/9): ")

if opcion in ['1', '2', '3', '4', '5']:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    elif opcion == '5':
        print("Resultado:", potencia(num1, num2))
elif opcion in ['6', '7', '8', '9']:
    num = float(input("Ingrese el número: "))
    if opcion == '6':
        print("Resultado:", raiz_cuadrada(num))
    elif opcion == '7':
        print("Seno:", seno(num))
    elif opcion == '8':
        print("Coseno:", coseno(num))
    elif opcion == '9':
        print("Tangente:", tangente(num))
else:
    print("Opción no válida")
