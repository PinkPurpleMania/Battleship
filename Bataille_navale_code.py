from random import *

grille1 =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

grille1_cachee =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

grille2 =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

grille2_cachee =  [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

#Fonction pour afficher une grille
def afficher(grille1,grille2):
    nom_ligne = [chr(65), chr(66), chr(67), chr(68), chr(69), chr(70), chr(71), chr(72), chr(73), chr(74)]  #A, B, C, D, E, F, G, H, I, J
    print("Ta grille\n    0   1   2   3   4   5   6   7   8   9")
    print("  -----------------------------------------")
    for i in range(len(grille1)):
        print(nom_ligne[i] + " | ", end="")
        for j in range(len(grille1[i])):
            print(grille1[i][j], end="")
            print(" | ", end="")
        print("\n  -----------------------------------------")
    print("\nLa grille de ton adversaire\n    0   1   2   3   4   5   6   7   8   9")
    print("  -----------------------------------------")
    for i in range(len(grille2)):
        print(nom_ligne[i] + " | ", end="")
        for j in range(len(grille2[i])):
            print(grille2[i][j], end="")
            print(" | ", end="")
        print("\n  -----------------------------------------")
    print("\n")

def coordonnees_valides(ligne,colonne):
    if (0<=ligne<=9) and (0<=colonne<=9):
        return True
    return False

def case_vide(grille, ligne, colonne):
    if grille[ligne][colonne] == ' ':
        return True
    return False

def pos_bateau_possible(pos, taille, grille, ligne, colonne):
    possible = 0
    if pos == 1:
        for i in range(taille):
            if case_vide(grille, ligne + i, colonne) == False:
                possible += 1
    if pos == 2:
        for i in range(taille):
            if case_vide(grille, ligne, colonne + i) == False:
                possible += 1
    if possible == 0:
        return True
    else:
        return False

#Fonction pour initialiser aléatoirement les grilles de jeu avec les bateaux
def positions_aleatoire_bateaux(grille):
    liste_bateaux = [5,4,3,3,2]
    for taille in liste_bateaux:
        pos = randint(1,2)  #position verticale(1) ou horizontale(2) du bateau à placer
        if pos == 1: #position verticale du bateau
            ligne = randint(0,(9-(taille-1)))
            colonne = randint(0,9)
            while pos_bateau_possible(pos,taille,grille,ligne,colonne)==False:
                ligne = randint(0,(9-(taille-1)))
                colonne = randint(0,9)
            for i in range (taille):
                grille[ligne+i][colonne]='B'
        if pos == 2: #position horizontale du bateau
            ligne = randint(0,9)
            colonne = randint(0,(9-(taille-1)))
            while pos_bateau_possible(pos,taille,grille,ligne,colonne)==False:
                ligne = randint(0,(9-(taille-1)))
                colonne = randint(0,9)
            for i in range(taille):
                grille[ligne][colonne+i]='B'
    return grille,

def conversion_ligne_entier(ligne):
    if ligne == chr(65):
        ligne = 0
    elif ligne == chr(66):
        ligne = 1
    elif ligne == chr(67):
        ligne = 2
    elif ligne == chr(68):
        ligne = 3
    elif ligne == chr(69):
        ligne = 4
    elif ligne == chr(70):
        ligne = 5
    elif ligne == chr(71):
        ligne = 6
    elif ligne == chr(72):
        ligne = 7
    elif ligne == chr(73):
        ligne = 8
    elif ligne == chr(74):
        ligne = 9
    else:
        ligne = 10
    return ligne

def changement_joueur_courant(joueur_courant):
    if joueur_courant == 1:
        joueur_courant += 1
    elif joueur_courant == 2:
        joueur_courant -= 1
    return joueur_courant

def afficher_joueur(joueur):
    if joueur == 1:
        print("A ton tour joueur 1")
    elif joueur == 2:
        print("A ton tour joueur 2")

def saisie_coordonnees(joueur,coordonnees_saisies1,coordonnees_saisies2):
    coordonnees = input("Saisir les coordonnées (exemple A2) : ")
    while (len(coordonnees)!=2):
        coordonnees = input("Saisir les coordonnées (exemple A2) : ")
    ligne = conversion_ligne_entier(coordonnees[0])
    colonne = int(coordonnees[1])
    if joueur == 1:
        while (len(coordonnees)!=2) or (coordonnees_valides(ligne,colonne)==False) or ((ligne,colonne) in coordonnees_saisies1):
            coordonnees = input("Saisir les coordonnées (exemple A2) : ")
            ligne = conversion_ligne_entier(coordonnees[0])
            colonne = int(coordonnees[1])
        coordonnees_saisies1.append((ligne,colonne))
    if joueur == 2:
        while (len(coordonnees)!=2) or (coordonnees_valides(ligne,colonne)==False) or ((ligne,colonne) in coordonnees_saisies2):
            coordonnees = input("Saisir les coordonnées (exemple A2) : ")
            ligne = conversion_ligne_entier(coordonnees[0])
            colonne = int(coordonnees[1])
        coordonnees_saisies2.append((ligne, colonne))
    return ligne,colonne

def bateau_touchee(grille,ligne,colonne):
    if grille[ligne][colonne]=="B":
        return True
    return False

def tour_de_jeu(joueur,grille1,grille2,grille1_cachee,grille2_cachee,liste_touchee1,liste_touchee2):
    if joueur == 1:
        afficher(grille1,grille2_cachee)
        afficher_joueur(joueur)
        ligne, colonne = saisie_coordonnees(joueur, coordonnees_saisies1, coordonnees_saisies2)
        if bateau_touchee(grille2, ligne, colonne) == True:
            print("Touchée\n")
            grille2_cachee[ligne][colonne] = "X"
            liste_touchee1.append((ligne,colonne))
        else:
            print("Manqué\n")
            grille2_cachee[ligne][colonne] = "*"
    if joueur == 2:
        afficher(grille2, grille1_cachee)
        afficher_joueur(joueur)
        ligne, colonne = saisie_coordonnees(joueur, coordonnees_saisies1, coordonnees_saisies2)
        if bateau_touchee(grille1, ligne, colonne) == True:
            print("Touchée\n")
            grille1_cachee[ligne][colonne] = "X"
            liste_touchee2.append((ligne,colonne))
        else:
            print("Manqué\n")
            grille1_cachee[ligne][colonne] = "*"
    joueur = changement_joueur_courant(joueur)
    return joueur,grille1,grille2,grille1_cachee,grille2_cachee,liste_touchee1,liste_touchee2

def fin_de_jeu(coordonnees1,coordonnees2,liste_touchee1,liste_touchee2):
    if (len(coordonnees2)) == (len(liste_touchee1)):
        for coord in liste_touchee1:
            if coord not in coordonnees2:
                return False
        return True
    if (len(coordonnees1))==(len(liste_touchee2)):
        for coord in liste_touchee2:
            if coord not in coordonnees1:
                return False
        return True
    if (len(coordonnees_saisies1)) == 100:
        return True
    if (len(coordonnees_saisies2)) == 100:
        return True
    return False

#Initialisation des listes
coordonnees_saisies1 = []
coordonnees_saisies2 = []
liste_touchee1 = []
liste_touchee2 = []

#Initialisation des positions aléatoires de chaque bateaux dans la grille de chaque joueur et du joueur courant
joueur = randint(1,2)
positions_aleatoire_bateaux(grille1)
positions_aleatoire_bateaux(grille2)
coordonnees1 = [] #Coordonnées des bateaux du joueur 1
coordonnees2 = [] #Coordonnées des bateaux du joueur 2
for i in range (len(grille1)):
    for j in range (len(grille1[i])):
        if grille1[i][j] == "B":
            coordonnees1.append((i,j))
for i in range (len(grille2)):
    for j in range (len(grille2[i])):
        if grille2[i][j] == "B":
            coordonnees2.append((i,j))

#lancement des tours de jeu jusqu'à la fin de partie
while fin_de_jeu(coordonnees1,coordonnees2,liste_touchee1,liste_touchee2)==False:
    joueur, grille1,grille2,grille1_cachee,grille2_cachee,liste_touchee1,liste_touchee2 = tour_de_jeu(joueur,grille1,grille2,grille1_cachee,grille2_cachee,liste_touchee1,liste_touchee2)

#afficher le gagnant
if joueur == 1:
    print("Joueur 2, you win !")
if joueur == 2:
    print("Joueur 1, you win !")
