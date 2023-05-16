# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(nbL: int, nbC: int) -> tuple:

    """
                Construit une coordonnée sous forme d'un tuple (nbL,nbC)

                :param nbL : variable qui représente la coordonnée x d'une cellule
                       nbC : variable qui représente la coordonnée y d'une cellule

                :return: la coordonnée
    """

    coord = (nbL, nbC)
    if type(nbL) != int or type(nbC) != int:
        raise TypeError(
            "construireCoordonnee: Le numéro de ligne",type(nbL), "ou le numéro de colonne" ,type(nbC),"ne sont pas des entiers")

    if nbL < 0 or nbC < 0:
        raise ValueError(
            "construireCoordonnee: Le numéro deligne", nbL ,"ou de colonne", nbC ,"ne sont pas positifs")

    return coord

def getLigneCoordonnee(coord : tuple) -> int :

    """
                Renvoie la ligne (coordonnée x) d'une case

                :param coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

                :return: renvoie la ligne de la coordonnée (nbL)
    """

    if type_coordonnee(coord) == False :
        raise TypeError(
            "getLigneCoordonnee : Le paramètre n’est pas une coordonnée")

    return coord[0]

def getColonneCoordonnee(coord : tuple) -> int :

    """
                Renvoie la colonne (coordonnée y) d'une case

                :param coord : variable qui représente les coordonnées d'une case sous un tuple (ligne,col)

                :return: renvoie la colonne de la coordonnée (nbC)
    """

    if type_coordonnee(coord) == False :
        raise TypeError(
            "getColonneCoordonnee : Le paramètre n’est pas une coordonnée")

    return coord[1]


