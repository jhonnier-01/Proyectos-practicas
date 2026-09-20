import random

numero = random.randint(1, 20)
contador = 6
intentos = 0
print("Bienvenido al juego de la adivinanza, intenta adivinar un numero dentro del rango del 1 al 20")
print("------------------------------------------------------------------------------------------------------------")
print("Ingrese un numero entre el 1 y el 20")
print("------------------------------------------------------------------------------------------------------------")
while True:
    try:
        adivinanza = int(input(f"Ingrese su numero, recuerde que solo tiene {contador} intentos, numero ingresado:  "))
        intentos += 1
        contador -= 1
        if adivinanza < numero:
            print("------------------------------------------------------------------------------------------------------------")
            print("El numero es mayor")
        elif adivinanza > numero:
            print("------------------------------------------------------------------------------------------------------------")
            print("El numero es menor")
        if contador == 0:
            print("------------------------------------------------------------------------------------------------------------")
            print(f"Se te acabaron los intentos :(, el numero era {numero})")
            break
        elif adivinanza == numero:
            print("------------------------------------------------------------------------------------------------------------")
            print(f"Enbuenahora, adivinaste el numero {numero} en {intentos} intentos")
            break
        else:
            print("------------------------------------------------------------------------------------------------------------")
            print("intenta de nuevo")
    except ValueError:
        print("------------------------------------------------------------------------------------------------------------")
        print("Ingrese un numero valido")
