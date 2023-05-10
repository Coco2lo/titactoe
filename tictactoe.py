import random
import time

# Fonction pour afficher la grille
def affichergrille():
    print("       0     1     2\n"
          "    ┏━━━━━┳━━━━━┳━━━━━┓\n"
          " 0  ┃  "+grille[0][0]+"  ┃  "+grille[0][1]+"  ┃  "+grille[0][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 1  ┃  "+grille[1][0]+"  ┃  "+grille[1][1]+"  ┃  "+grille[1][2]+"  ┃\n"
          "    ┣━━━━━╋━━━━━╋━━━━━┫\n"
          " 2  ┃  "+grille[2][0]+"  ┃  "+grille[2][1]+"  ┃  "+grille[2][2]+"  ┃\n"
          "    ┗━━━━━┻━━━━━┻━━━━━┛\n")

# Fonction pour placer le symbole dansla grille
def placerSymbole( ligne, col, symbole):
    grille[ligne][col] = symbole
    lastCasesLibre.remove((ligne,col))

def afficherSeparateur():
    print("----------------------------")

def ifCaseLibre(ligne, col):
    if (grille[ligne][col]) == "_":
        return True
    return False

def verifVictoire(symbole):
    if grille[0][0] == grille[0][1] == grille[0][2] == symbole or grille[1][0] == grille[1][1] == grille[1][2] == symbole or grille[2][0] == grille[2][1] == grille[2][2] == symbole:
        return True
    elif grille[0][0] == grille[1][0] == grille[2][0] == symbole or grille[0][1] == grille[1][1] == grille[2][1] == symbole or grille[0][2] == grille[1][2] == grille[2][2] == symbole:
        return True
    elif grille[0][0] == grille[1][1] == grille[2][2] == symbole or grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False


jeu = True
rejouer = "O"

afficherSeparateur()
print("Bienvenu dans le jeu du morpion ! \n"
      "Règle du jeu : \n"
      "Pour gagner il faut aligner trois de vos symboles :\n"
      "- Sur une même ligne\n"
      "- Sur une même colonne\n"
      "- Sur une même diagonale")

afficherSeparateur()

joueur1= {"prenom":"","symbole":"X"}
joueur2= {"prenom":"","symbole":"O"}

while rejouer == "O":
    grille = [["_" for _ in range(3)] for _ in range(3)]
    lastCasesLibre = [(x,y) for x in range(3) for y in range(3)]
    joueur1["prenom"] = input("Entrez le prénom du joueur 1: ")
    joueur2["prenom"] = input("Entrez le prénom du joueur 2: ")
    afficherSeparateur()
    print(joueur1["prenom"]," tu joueras les X")
    print(joueur2["prenom"], " tu joueras les O")
    afficherSeparateur()
    print("Un tirage au sort va désigner l'ordre pour commencer.")
    joueuractuel = random.choice([joueur1,joueur2])
    time.sleep(2)
    afficherSeparateur()
    while True:
        print(joueuractuel["prenom"]," à ton tour !")
        affichergrille()
        while True:
            while True:
                col = int(input("Quelle colonne souhaites tu jouer ? "))
                if col not in [0,1,2]:
                    print("Cette colonne n'existe pas !")
                else:
                    break
            while True:
                ligne = int(input("Quelle ligne souhaites tu jouer ? "))
                if ligne not in [0,1,2]:
                    print("Cette ligne n'existe pas !")
                else:
                    break

            # Vérification si la case est libre
            if ifCaseLibre(ligne, col):
                break
            else:
                print("Cette case est déjà prise !")

        placerSymbole(ligne, col, joueuractuel["symbole"])

        afficherSeparateur()

        #vérification de victoire
        if verifVictoire(joueuractuel["symbole"]):
            affichergrille()
            print("Bravo, ", joueuractuel["prenom"]," tu as gagné !")
            break

        if len(lastCasesLibre) == 0:
            affichergrille()
            afficherSeparateur()
            print("Egalité ! Toutes les cases ont été remplis. ")
        # changement du joueur
        if joueuractuel == joueur1:
            joueuractuel = joueur2
        else :
            joueuractuel = joueur1

    rejouer = "X"
    while rejouer not in ["O", "N"]:
        afficherSeparateur()
        rejouer = input("Souhaitez-vous rejouer ? [O/N]")
    if rejouer == "N":
        break

afficherSeparateur()
print("A bientôt !")
afficherSeparateur()