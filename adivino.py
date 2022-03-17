import random

# en la practica dice entre 0 y 100 asi que cambie el randrange hasta 101 y el print
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 3 intentos para adivinar un entre 0 y 100")
intento = 0
while intento < 5 and not gane:
    numero_ingresado = int(input("Ingresa tu número: "))
    if numero_ingresado == numero_aleatorio:
        print("Ganaste! y necesitaste {} intentos!!!".format(intento))
        gane = True
    else:
        print("Mmmm ... No.. ese número no es... Seguí intentando.")
        intento += 1
if not gane:
    print("\n Perdiste :(\n El número era: {}".format(numero_aleatorio))
