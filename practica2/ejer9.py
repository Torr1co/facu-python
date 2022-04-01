minas = [
    "-*-*-",
    "--*--",
    "----*",
    "*----",
]

minas = [list(col) for col in minas]

# no son utilizadas pero en un proyecto real seria lo mejor
MAX_ROW = 3
MAX_COL = 4


def setNumber(rowI, colI):
    cant = 0

    startRow = 0 if rowI == 0 else -1
    endRow = 1 if rowI == 3 else 2

    startCol = 0 if colI == 0 else -1
    endCol = 1 if colI == 4 else 2

    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            if minas[rowI + i][colI + j] == "*":
                cant += 1
    return cant


for row in range(len(minas)):
    for col in range(len(minas[row])):
        if minas[row][col] != "*":
            minas[row][col] = setNumber(row, col)
    "".join(str(mina) for mina in minas[row])

for mina in minas:
    print(mina)
