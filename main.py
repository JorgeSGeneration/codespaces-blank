#este es un comentario

myName = input("ingresa tu nombre: ")
myLastName = input("ingresa tu apellido: ")
print(f"Binevenido {myName} {myLastName} a la página web :)")

print("quieres sumar?: ")

def sumar(x, y):
    return x + y

#solicitar al usuario que ingrese los dos números
numero1 = float(input("Introduce al primer numero: "))
numero2 = float(input("Introduce al segundo numero: "))
resultado = sumar(numero1, numero2)
#mostrar el resultado
print(resultado)