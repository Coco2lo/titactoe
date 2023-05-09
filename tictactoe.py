grille = [["_" for _ in range(3)] for _ in range(3)]

print (grille)

def affichergrille():
    print("       0     1     2\n"
          "    ┏━━━━━┳━━━━━┳━━━━━┓\n"
          " 0  ┃  "+grille[0][0]+"  ┃  "+grille[0][1]+"  ┃  "+grille[0][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 1  ┃  "+grille[1][0]+"  ┃  "+grille[1][1]+"  ┃  "+grille[1][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 2  ┃  "+grille[2][0]+"  ┃  "+grille[2][1]+"  ┃  "+grille[2][2]+"  ┃\n"
          "    ┗━━━━━┻━━━━━┻━━━━━┛\n")

def placerSymbole( col, ligne, symbole):
    grille[ligne][col] = symbole


affichergrille()

placerSymbole(0,2,"X")
affichergrille()