one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
two = ["D", "G"]
three = ["B", " C", "M", "P"]
four = ["F", "H", "V", "W", "Y "]
five = ["K"]
eigth = ["J", "X "]
ten = ["Q", "Z "]

puntos = (
    {c: 1 for c in one}
    | {c: 2 for c in two}
    | {c: 3 for c in three}
    | {c: 4 for c in four}
    | {c: 5 for c in five}
    | {c: 8 for c in eigth}
    | {c: 10 for c in ten}
)

texto = input('Escriba una palabra para conocer sus puntos:')
total = 0
for char in texto.upper():
    total += puntos[char]
print(total)
