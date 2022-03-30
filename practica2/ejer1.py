with open("readme.txt", "rt") as f:
    query = [line for line in f.readlines() if ("http" or "https") in line]
    print(query)

# chequear donde se encuentra ubicado en la terminal al correr el codigo
# hay algunos comentarios y variables en ingles ya que suelo programar en ese idioma, me disculpo