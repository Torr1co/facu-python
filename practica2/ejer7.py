from collections import Counter

palabra = input("ingrese una palabra: ").lower()
if (palabra):
    print(Counter(palabra).most_common()[0][1] == 1 )
