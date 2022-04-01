from collections import Counter

frase = input("ingrese una frase: ").lower()
palabra = input("ingrese una palabra: ").lower()

print(Counter(frase.split())[palabra])


# parte 2
cadena = input(
    """Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):"""
)

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif map(lambda c: c in cadena, ("@" or "!")):
    print("Ingresaste alguno de estos símbolos: @ o !")
else:
    print("Clave válida")
