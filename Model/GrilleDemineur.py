# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:

    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nl : int, nc : int) -> list :

    """
            Construit la grille de notre démineur

            :param nl : variable qui représente le nombre de ligne dans la grille
                   nc : variable qui représente le nombre de colonne dans la grille


            :return: la grille (c'est une list avec des list dedans)
    """

    lstGrille = []
    if type(nl) != int or type(nc) != int :
        raise TypeError("construireGrilleDemineur : Le nombre de lignes", type(nl)," ou de colonnes", type(nc)," n’est pas un entier.")
    if nl <= 0 or nc <= 0 :
        raise ValueError("construireGrilleDemineur : Le nombre de lignes", nl," ou de colonnes", nc," est négatif ou nul.")

    for ligne in range(nl):
        lstTemp = []
        for col in range(nc):
            lstTemp = lstTemp + [construireCellule()]    #je commence par créer la première ligne puis toutes les colonnes de cette première ligne et ainsi de suite

        lstGrille = lstGrille + [lstTemp]

    return lstGrille


def getNbLignesGrilleDemineur(lstGrille : list) -> int :

    """
            Donne le nombre de ligne de la grille

            :param lstGrille : variable qui représente la grille


            :return: le nombre de ligne de la grille
    """

    if type_grille_demineur(lstGrille) == False :
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")

    return len(lstGrille)


def getNbColonnesGrilleDemineur(lstGrille : list) -> int :

    """
            Donnele nombre de colonne de la grille

            :param lstGrille : variable qui représente la grille


            :return: le nombre de colonne de la grille
    """

    if type_grille_demineur(lstGrille) == False :
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")

    return len(lstGrille[0])


def isCoordonneeCorrecte(lstGrille : list, coord : tuple) -> bool :

    """
            Vérifie si la coordonnée passée en paramètre est correcte (si elle se trouve dans la grille)

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)


            :return: True si oui, False sinon
    """

    coordPresente = False

    if type_grille_demineur(lstGrille) == False or type_coordonnee(coord) == False  :
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    if getLigneCoordonnee(coord) < getNbLignesGrilleDemineur(lstGrille) and getColonneCoordonnee(coord) < getNbColonnesGrilleDemineur(lstGrille):
        # en effet la coordonnée ne doit pas être supérieur aux bords maximum car sinon elle serait en dehors de la grille
        coordPresente = True

    return coordPresente


def getCelluleGrilleDemineur(lstGrille : list, coord : tuple) -> dict :

    """
            Donne la cellule (son contenu/annotation/visibilité/resolu)

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: cellule
    """

    if type_grille_demineur(lstGrille) == False or type_coordonnee(coord) == False:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")

    if isCoordonneeCorrecte(lstGrille,coord) == False :
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")

    return lstGrille[coord[0]][coord[1]]


def getContenuGrilleDemineur(lstGrille : list, coord : tuple) -> dict :

    """
            Donne le contenu d'une cellule de la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: contenu de la celulle
    """

    return getContenuCellule(getCelluleGrilleDemineur(lstGrille,coord))


def setContenuGrilleDemineur(lstGrille : list, coord : tuple, contenu : int) :

    """
            Change le contenu d'une cellule présente dans la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)
                   contenu : variable qui représente le nombre de mine autour de cette case

            :return: change le contenu de la cellule
    """

    return setContenuCellule(getCelluleGrilleDemineur(lstGrille, coord), contenu)


def isVisibleGrilleDemineur(lstGrille : list, coord : tuple) -> dict :

    """
            Donne la visibilité d'une cellule présente dans la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: True si oui False sinon
    """

    return isVisibleCellule(getCelluleGrilleDemineur(lstGrille,coord))


def setVisibleGrilleDemineur(lstGrille : list, coord : tuple, visibilite : bool) -> dict :

    """
            Change la visibilité d'une cellule présente dans la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)
                   visibilite: variable qui représente si la case est visible ou non (True si oui, False sinon)


            :return: change la visibilité de la cellule
    """

    return setVisibleCellule(getCelluleGrilleDemineur(lstGrille,coord),visibilite)


def contientMineGrilleDemineur(lstGrille : list, coord : tuple) -> bool :

    """
            Retourne True si la cellule contient une mine, False sinon

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: True ou False
    """

    return contientMineCellule(getCelluleGrilleDemineur(lstGrille,coord))


def getCoordonneeVoisinsGrilleDemineur(lstGrille : list, coord : tuple) -> list :

    """
            Donne les coordonnées voisines d'une cellule de la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: list des coordonnées voisines de la cellule
    """

    lstCoordVoisin = []

    if type_grille_demineur(lstGrille) == False or type_coordonnee(coord) == False :
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")

    if isCoordonneeCorrecte(lstGrille,coord) == False :
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")

    # ici je n'optimise pas vraiment le code, je n'ai pas réussi à faire mieux : une case a au maximum 8 cases autour d'elle, je parcours ces 8 cases et je vérifie si elles existent bien
    # avec isCoordonneeCorrecte

    # case juste au dessus de la coord passée en paramètre
    if getLigneCoordonnee(coord)-1>=0 and isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord))) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord))]

    # case en haut à gauche de la coord passée en paramètre
    if getLigneCoordonnee(coord)-1>=0 and getColonneCoordonnee(coord)-1>=0 and isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord)-1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord)-1)]

    # case en haut à gauche de la coord passée en paramètre
    if getLigneCoordonnee(coord)-1>=0 and isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord)+1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)-1,getColonneCoordonnee(coord)+1)]

    # case à gauche de la coord passée en paramètre
    if getColonneCoordonnee(coord)-1>=0 and isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord),getColonneCoordonnee(coord)-1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord),getColonneCoordonnee(coord)-1)]

    # case à droite de la coord passée en paramètre
    if isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord),getColonneCoordonnee(coord)+1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord),getColonneCoordonnee(coord)+1)]

    # case en bas à gauche de la coord passée en paramètre
    if getColonneCoordonnee(coord)-1>=0 and isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord)-1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord)-1)]

    # case juste en dessous de la coord passée en paramètre
    if isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord))) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord))]

    # case en bas à droite de la coord passée en paramètre
    if isCoordonneeCorrecte(lstGrille,(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord)+1)) == True :
        lstCoordVoisin = lstCoordVoisin + [(getLigneCoordonnee(coord)+1,getColonneCoordonnee(coord)+1)]


    return lstCoordVoisin


def placerMinesGrilleDemineur(lstGrille : list, nb : int, coord : tuple):

    """
            Place nb mines dans la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)
                   nb : variable qui représente le nombre de mine à placer

            :return: rien
    """

    if isCoordonneeCorrecte(lstGrille,coord) == False :
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")


    if (nb < 0) or (nb > len(lstGrille)*len(lstGrille[0])-1):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")


    minePlacer = []
    minePlacerInt = 0

    #tant que je n'ai pas placer le nombre de mine demandé je continue
    while minePlacerInt < nb :

        #je tire une coord random dans ma grille
        randomCoord = (randint(0,len(lstGrille)-1),randint(0,len(lstGrille[0])-1))

        #si elle ne correspond pas à la case cliqué (car la première case ne peut pas contenir de mine) et que la case n'a pas déjà une mine (donc dans ma lst de minePlacer)
        if randomCoord != coord and randomCoord not in minePlacer:

                setContenuCellule(lstGrille[getLigneCoordonnee(randomCoord)][getColonneCoordonnee(randomCoord)],const.ID_MINE)
                minePlacer.append(randomCoord)
                minePlacerInt += 1

    compterMinesVoisinesGrilleDemineur(lstGrille)
    return


def compterMinesVoisinesGrilleDemineur(lstGrille : list):

    """
            Pour toutes les cases de la grille, la fonction compte les mines voisines et remplace le contenu de la case par ce nombre

            :param lstGrille : variable qui représente la grille

            :return: rien
    """
    #je parcours toutes mes cases de la grille
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):

            #si la case n'est pas une mine, je récupère ses coordonnées voisines
            if getContenuCellule(lstGrille[ligne][col]) != const.ID_MINE :
                lstCoordVoisin = getCoordonneeVoisinsGrilleDemineur(lstGrille,(ligne,col))

                #je parcours toutes les cases des cases voisines et si elles ont une mine, le contenu de ma case de base devient son contenu+1
                for element in range(len(lstCoordVoisin)):

                    if getContenuCellule(lstGrille[lstCoordVoisin[element][0]][lstCoordVoisin[element][1]]) == const.ID_MINE :

                       contenu = getContenuCellule(lstGrille[ligne][col])+1
                       setContenuCellule(lstGrille[ligne][col], contenu)

    return


def getNbMinesGrilleDemineur(lstGrille : list) -> int :

    """
            Donne le nombre de mine dans la grille

            :param lstGrille : variable qui représente la grille

            :return: le nombre de mine dans la grille
    """

    if type_grille_demineur(lstGrille) == False :
        raise ValueError("« getNbMinesGrilleDemineur : le paramètre n’est pas une grille")

    nbMinesGrille = 0

    #je parcours toutes mes cases
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):

            #si le contenu d'une case vaut const.ID_MINE cela veut dire que c'est une mine donc j'intende le compteur
            if getContenuCellule(lstGrille[ligne][col]) == const.ID_MINE :
                nbMinesGrille += 1

    return nbMinesGrille


def getAnnotationGrilleDemineur(lstGrille : list, coord : tuple) -> str:

    """
            Donne l'annotation d'une cellule de la grille

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: l'annotation de la cellule
    """

    return getAnnotationCellule(getCelluleGrilleDemineur(lstGrille,coord))


def getMinesRestantesGrilleDemineur(lstGrille : list) -> int :

    """
            Donne le nombre de mine restante dans la grille

            :param lstGrille : variable qui représente la grille

            :return: le nombre de mine restante dans la grille
    """

    nb = 0

    #je parcours toutes mes cases
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):

            #si la case a l'annotation FLAG donc qu'on soupçonne une mine, j'intende le compteur
            if getAnnotationCellule(lstGrille[ligne][col]) == const.FLAG:
                nb +=1

    #et à la fin pour savoir les mines potentiellement restantes j'appelle la fonction qui me donne le nombre de mine de la grille et je le soustrait par mon nombre de flag dans la grille
    return getNbMinesGrilleDemineur(lstGrille)-nb


def gagneGrilleDemineur(lstGrille : list) -> bool :

    """
            Vérifie si la partie est gagnée

            :param lstGrille : variable qui représente la grille

            :return: True si le joueur a gagné, False sinon
    """

    gagner = True

    #je parcours toutes mes cases
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):

            if getContenuCellule(lstGrille[ligne][col]) != -1 and isVisibleCellule(lstGrille[ligne][col]) == False or getContenuCellule(lstGrille[ligne][col]) == const.ID_MINE and isVisibleCellule(lstGrille[ligne][col]) == True and getAnnotationCellule(lstGrille[ligne][col]) == const.FLAG  :
                gagner = False


    return gagner


def perduGrilleDemineur(lstGrille : list) -> bool :

    """
            Vérifie si la partie est perdu (découvre une bombe)

            :param lstGrille : variable qui représente la grille

            :return: True si le joueur a perdu, False sinon
    """

    perdu = False

    #je parcours toutes mes cases
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):

            # si c'est une mine et qu'elle est visible cela veut dire qu'on a cliqué sur une mine --> on a donc perdu
            if getContenuCellule(lstGrille[ligne][col]) == -1 and isVisibleCellule(lstGrille[ligne][col]) == True :

                    perdu = True

    return perdu


def reinitialiserGrilleDemineur(lstGrille : list) :

    """
            Reinitialise toute la grille (le jeu par conséquent), la fonction reinitialise 1 par 1 les cases du démineur

            :param lstGrille : variable qui représente la grille

            :return: rien
    """

    # je parcours toutes mes cases et reinitialise une par une mes cases
    for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
        for col in range(getNbColonnesGrilleDemineur(lstGrille)):
            reinitialiserCellule(lstGrille[ligne][col])

    return


def decouvrirGrilleDemineur(lstGrille : list, coord : tuple):

    """
            Cette fonction permet de découvrir plus facilement et automatiquement la grille, elle résout la grille mais pas totalement

            :param lstGrille : variable qui représente la grille
                   coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

            :return: un ensemble des cases découvertes
    """

    #je commence par créer un ensemble s vide
    s = set()
    lstCoordVoisinUse = []
    setVisibleCellule(lstGrille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)],True)
    s.add(coord)

    #si le contenu de la case cliqué vaut 0, c'est à dire qu'elle n'a aucune mine autour d'elle
    if getContenuCellule(lstGrille[getLigneCoordonnee(coord)][getColonneCoordonnee(coord)]) == 0 :

        #je prends ses coordonnées voisines et ajoute la coord passé en paramètre à une liste qui correspond aux coords que j'ai déjà simplifié
        lstCoordVoisin = getCoordonneeVoisinsGrilleDemineur(lstGrille, coord)
        lstCoordVoisinUse.append(coord)

        #pour le nombre de cases voisines
        for indice in range(len(lstCoordVoisin)):

            #si elles ne sont pas visibles, je les mets visible et je les ajoute à l'ensemble
            if isVisibleGrilleDemineur(lstGrille,lstCoordVoisin[indice]) == False :

                setVisibleGrilleDemineur(lstGrille,lstCoordVoisin[indice],True)
                s.add((getLigneCoordonnee(lstCoordVoisin[indice]),getColonneCoordonnee(lstCoordVoisin[indice])))

        #ici je fais une boucle while pour reitérer le cheminement fait juste au dessus pour chaque case voisine qui ont un contenu == 0, puis je récupère donc ses cases voisines et ainsi de suite
        coordAjouter = True

        #le bool coordAjouter et temp me permettent de mettre fin à la boucle, au début de la boucle je récupère la longueur de ma liste de cases voisines
        #si à la fin de ma boucle ma longueur de cases voisines et égale à celle du début, cela veut dire que je n'ai plus aucune cases à simplifier et donc ma boucle s'arrête
        while coordAjouter == True:
            temp = len(lstCoordVoisin)

            #je parcours toute ma liste de coords voisines
            for element in range(temp):

                #si le contenu de la case vaut 0, c'est à dire qu'elle n'a aucune mine autour d'elle et que je ne l'ai pas encore simplifié
                #je l'ajoute à mes coords voisines et j'ajoute cette coord à ma liste simplifié
                if getContenuGrilleDemineur(lstGrille, lstCoordVoisin[element]) == 0 and lstCoordVoisin[element] not in lstCoordVoisinUse:
                    lstCoordVoisin = lstCoordVoisin + getCoordonneeVoisinsGrilleDemineur(lstGrille, lstCoordVoisin[element])
                    lstCoordVoisinUse.append(lstCoordVoisin[element])

                    #et je finis par mettre ces cases visibles et je les ajoute à mon ensemble
                    for coordonnee in range(len(lstCoordVoisin)):
                        setVisibleGrilleDemineur(lstGrille, lstCoordVoisin[coordonnee], True)
                        s.add((getLigneCoordonnee(lstCoordVoisin[coordonnee]), getColonneCoordonnee(lstCoordVoisin[coordonnee])))

            #if pour vérifier si ma boucle while doit se finir ou non fin
            if temp == len(lstCoordVoisin):
                coordAjouter = False


    return s


def simplifierGrilleDemineur(lstGrille : list, coord : tuple):

    """
                En fonction des flags mis, cette fonction va simplifer la grille et donc découvrir des cases où il n'y a pas de mine

                :param lstGrille : variable qui représente la grille
                       coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

                :return: un ensemble des cases simplifier
    """

    # je commence par créer un ensemble s vide
    s = set()
    lstCoordASimplifier = []

    #si la coord passé en paramètre est visible, je récupère ses coords voisines
    if isVisibleCellule(lstGrille[coord[0]][coord[1]]) == True:

        lstCoordVoisin = getCoordonneeVoisinsGrilleDemineur(lstGrille,coord)
        nbFlag = 0

        #pour toutes les cases voisines, si elles ont un FLAG j'intende mon compteur
        for coordonnee in range(len(lstCoordVoisin)):
            if getAnnotationCellule(lstGrille[lstCoordVoisin[coordonnee][0]][lstCoordVoisin[coordonnee][1]]) == const.FLAG :
                nbFlag += 1

        #si le nbFlag autour de la casse passé en paramètre et égale au contenu de cette case, je reparcours toutes les cases voisines
        if nbFlag == getContenuCellule(lstGrille[coord[0]][coord[1]]):
            for element in range(len(lstCoordVoisin)):

                #et si elles n'ont pas de FLAG donc potentiellement pas de mine, je les rends visible et les ajoute à mon ensemble
                if getAnnotationCellule(lstGrille[lstCoordVoisin[element][0]][lstCoordVoisin[element][1]]) != const.FLAG :
                    setVisibleGrilleDemineur(lstGrille,lstCoordVoisin[element],True)
                    s.add(lstCoordVoisin[element])
                    lstCoordASimplifier.append(lstCoordVoisin[element])

    #je vérifie si j'ai au moins une coord à simplifier
    if len(lstCoordASimplifier) != 0:
        changer = True
        while changer == True :

            #ici la variable temp va me servir à la fin de la boucle pour savoir si je mets fin à la boucle oui ou non
            temp = len(lstCoordASimplifier)

            #je reset mon nbFlag et prend les coords voisines
            for element in range(len(lstCoordASimplifier)):

                nbFlag = 0
                lstCoordVoisin = getCoordonneeVoisinsGrilleDemineur(lstGrille,lstCoordASimplifier[element])

                #je parcours le nombre de case voisine, je vérifie si elles ont un FLAG, si oui je fais +1 a nbFlag
                for nbCaseMax in range(len(lstCoordVoisin)):
                    if getAnnotationGrilleDemineur(lstGrille,lstCoordVoisin[nbCaseMax]) == const.FLAG :
                        nbFlag +=1

                #si le nombre de flag autour de la case est égale au contenu
                #je reparcours la liste des coordVoisines et si elles ne sont pas visibles et qu'elles n'ont pas le FLAG, je les rends visible et les ajoute à mon ensemble
                if nbFlag == getContenuGrilleDemineur(lstGrille,lstCoordASimplifier[element]):
                    for coord in range(len(lstCoordVoisin)):
                        if isVisibleGrilleDemineur(lstGrille,lstCoordVoisin[coord]) == False and getAnnotationGrilleDemineur(lstGrille,lstCoordVoisin[coord]) != const.FLAG :
                            setVisibleGrilleDemineur(lstGrille,lstCoordVoisin[coord],True)

                            #j'ajoute la coord que j'ai rendu visible à la liste de coord à simplifier pour la simplifier ensuite dans ma boucle while
                            lstCoordASimplifier.append(lstCoordVoisin[coord])
                            s.add(lstCoordVoisin[coord])

            # if pour vérifier si ma boucle while doit se finir ou non fin
            if len(lstCoordASimplifier) == temp:
                changer = False


    return s


def ajouterFlagsGrilleDemineur(lstGrille: list, coord:tuple) -> set:
    """
        Cette fonction permet d'ajouter des drapeaux sur des cases où cela est évident

        :param lstGrille : variable qui représente la grille
               coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

        :return: un ensemble des cases où l'on a mis un drapeau
    """

    #je commence par créer un ensemble vide
    s = set()
    nbCaseNonDecouverte = 0
    lstNbCaseNonDecouverte = []
    lstCoordVoisin = getCoordonneeVoisinsGrilleDemineur(lstGrille,coord)

    #je parcours mes cases voisines et si une n'est pas visible ou qu'elle est un drapeau, j'intende de 1 nbCaseNonDecouverte et l'ajoute à ma lst correspondante
    for caseVoisine in range(len(lstCoordVoisin)):
        if isVisibleGrilleDemineur(lstGrille,lstCoordVoisin[caseVoisine]) == False or getAnnotationGrilleDemineur(lstGrille,lstCoordVoisin[caseVoisine]) == const.FLAG:

            nbCaseNonDecouverte += 1
            lstNbCaseNonDecouverte.append(lstCoordVoisin[caseVoisine])

    #si le contenu de la coord passé en paramètre vaut le nombre de case non découverte du voisinage je parcours ma lstNbCaseNonDecouverte
    if getContenuGrilleDemineur(lstGrille,coord) == nbCaseNonDecouverte:
        for coordNonDecouverte in range(len(lstNbCaseNonDecouverte)):

            #si l'annotation de cette case vaut None, je fais un changeAnnotation pour la passer en flag (None -> Flag -> Doute) et je l'ajoute à mon ensemble
            if getAnnotationGrilleDemineur(lstGrille,lstNbCaseNonDecouverte[coordNonDecouverte]) == None:

                changeAnnotationCellule(lstGrille[getLigneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])][getColonneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])])
                s.add(lstNbCaseNonDecouverte[coordNonDecouverte])

            # si l'annotation de cette case vaut Doue, je fais deux changeAnnotation pour la passer en flag (None -> Flag -> Doute) et je l'ajoute à mon ensemble
            if getAnnotationGrilleDemineur(lstGrille,lstNbCaseNonDecouverte[coordNonDecouverte]) == const.DOUTE:

                changeAnnotationCellule(lstGrille[getLigneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])][getColonneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])])
                changeAnnotationCellule(lstGrille[getLigneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])][getColonneCoordonnee(lstNbCaseNonDecouverte[coordNonDecouverte])])
                s.add(lstNbCaseNonDecouverte[coordNonDecouverte])

    return s


def simplifierToutGrilleDemineur(lstGrille: list) -> tuple:
    """
            Cette fonction permet de simplifier automatiquement la grille entière à l'aide d'un algorithme et de fonctions précédentes

            :param lstGrille : variable qui représente la grille


            :return: un tuple des coord que j'ai simplifié au maximum
        """

    #je commence par créer deux ensembles, un pour les coords où j'ajoute un drapeau, l'autre pour les coords que je simplifie
    s_simplifie = set()
    s_ajoute = set()

    changement = True

    while changement == True :

        #à chaque boucle de while je récupère les longueurs de mes 2 ensembles pour les comparés ensuite à la fin du while, cela me permet de mettre fin à la boucle
        longueurEnsembleSimplifie = len(s_simplifie)
        longueurEnsembleAjoute = len(s_ajoute)

        #pour toutes les cases de ma grille
        for ligne in range(getNbLignesGrilleDemineur(lstGrille)):
            for col in range(getNbColonnesGrilleDemineur(lstGrille)):

                #si la case n'a pas encore été résolu je l'ajoute à deux variables temporaires qui vont me servir pour la résoudre
                if getResoluCellule(lstGrille[ligne][col]) == False:

                    tempEnsembleSimplifie = list(simplifierGrilleDemineur(lstGrille, (ligne, col)))
                    tempEnsembleAjoute = list(ajouterFlagsGrilleDemineur(lstGrille,(ligne,col)))

                    #je vérifie au cas où si tempEnsembleAjoute n'est pas vide et je parcours toutes les coords de tempEnsembleAjoute (donc toutes les coords où j'ai placer un drapeau)
                    #je commence par tempEnsembleAjoute car j'ajoute d'abord mes drapeaux puis je lance la simplification !
                    if len(tempEnsembleAjoute) != 0:
                        for coord in tempEnsembleAjoute:
                            s_ajoute.add(coord)

                    #je vérifie au cas où si tempEnsembleSimplifie n'est pas vide et je parcours toutes les coords de tempEnsembleSimplifie (donc toutes les coords que j'ai simplifier)
                    if len(tempEnsembleSimplifie) != 0:
                        for coord in tempEnsembleSimplifie:
                            s_simplifie.add(coord)

                #je parcours l'ensemble simplifie et je vérifie quand même si je lui ai passé la fonction ajouterFlag, si la coord est dans mon ensemble s_ajouter cela veut dire qu'elle est résolu
                #je ne peux plus la simplifier donc je change const.RESOLU à True !
                for temp in s_simplifie:
                    if temp in s_ajoute:
                        setResoluCellule(lstGrille[getLigneCoordonnee(temp)][getColonneCoordonnee(temp)],True)

        #if qui me permet d'arrêter la boucle, si les longueurs de mes ensembles sont identiques à ceux du début de boucle cela veut dire qu'il n'y a rien à simplifier
        #donc soit la partie est gagné soit je dois aider l'algorithme car il hésite entre deux cases
        if longueurEnsembleSimplifie == len(s_simplifie) and longueurEnsembleAjoute == len(s_ajoute):
            changement = False


    return(s_simplifie,s_ajoute)













