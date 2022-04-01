archNombres = open("nombres.txt", "r", encoding="utf-8")
archNombres2 = open("nombres2.txt", "r", encoding="utf-8")
archEval1 = open("eval1.txt", "r", encoding="utf-8")
archEval2 = open("eval2.txt", "r", encoding="utf-8")

nombres = set(archNombres.read().lower().split())
nombres2 = set(archNombres2.read().lower().split())
eval1 = archEval1.read().split(",")
eval2 = archEval2.read().split(",")

# MAIN
nombresRepetidos = [n for n in nombres for n2 in nombres2 if n == n2]
print("nombres repetidos:", nombresRepetidos)

# para imprimir mas bonito
print("   {:<15} {:<10} {:<10} {:<10}".format("NOMBRE", "EVAL1", "EVAL2", "TOTAL"))
for i, estudiante in enumerate(zip(nombres, eval1, eval2)):
    nombre, nota1, nota2 = estudiante
    nota1, nota2 = int(nota1), int(nota2)

    print(
        "{:<} {:<18} {:<10} {:<10} {:<10}".format(
            i, nombre, nota1, nota2, nota1 + nota2
        )
    )

archNombres.close()
archNombres2.close()
archEval1.close()
archEval2.close()
