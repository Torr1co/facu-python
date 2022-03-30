from collections import Counter

with open("readme.txt", "r") as text:
    words = set(text.read().lower().split())
    myChar = input("Escriba una letra...: ")
    if (myChar):
        for word in words:
            if word.startswith(myChar):
                print(word)
    else:
        print('no has ingresado ninguna letra')
