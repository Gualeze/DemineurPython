# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:

    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """

    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(contenu: int) -> bool:

    """
        Détermine si le contenu est correct

        :param contenu: variable qui représente le contenu d'une cellule (0 si il y a 0 mine autour de lui, 5 si il a 5 mines autour de lui, etc...)

        :return: True si c'est un contenu correct, False sinon
        """

    ContenuCorrectBool = False

    if type(contenu) == int :
        if (contenu >= 0 and contenu <= 8) or contenu == const.ID_MINE:
            ContenuCorrectBool = True

    return ContenuCorrectBool


def construireCellule(contenu: int = 0, visible: bool = False, annotation : str = None, resolu : bool = False) -> dict:

    """
            Construit une cellule(case) de la grille

            :param contenu: variable qui représente le nombre de mine autour de cette case / VALEUR PAR DEFAUT = 0
                   visible: variable qui représente si la case est visible ou non (True si oui, False sinon) / VALEUR PAR DEFAUT = False
                   annotation : variable qui représente l'annotation présente sur la case ( None. flag, doute) / VALEUR PAR DEFAUT = None
                   resolu : variable qui représente si la simplification qui dépend de cette case a été fait (True si oui, False sinon) / VALEUR PAR DEFAUT = False

            :return: cell qui vient d'être construit
            """

    if isContenuCorrect(contenu) == False:
        raise ValueError("construireCellule : le contenu", contenu, "n’est pas correct")

    if type(visible) != bool:
        raise TypeError("construireCellule : le second paramètre", visible, "n’est pas un booléen")

    cell = {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION : annotation, const.RESOLU : resolu}

    return cell


#les 2 fonctions ci-dessous ont été créé par moi même, elle vise à optimiser la simplification de la grille
def getResoluCellule(cell : dict) -> bool :

    """
            Donne la valeur de const.RESOLU dans la cellule

            :param cell : variable qui représente une case


            :return: la valeur de const.RESOLU d'une case
    """

    return cell[const.RESOLU]


def setResoluCellule(cell : dict, resolu : bool) -> None:

    """
            Changer la valeur de const.RESOLU d'une cellule

            :param cell : variable qui représente une case
                   resolu : variable qui représente la valeur qu'on va donner à const.RESOLU (True or False)


            :return: rien
    """

    cell[const.RESOLU] = resolu

    return


def getContenuCellule(cell: dict) -> int:

    """
            Donne la valeur de const.CONTENU dans la cellule

            :param cell : variable qui représente une case


             :return: la valeur de const.CONTENU d'une case
    """

    if type_cellule(cell) == False:
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule.")

    return cell[const.CONTENU]


def isVisibleCellule(cell: dict) -> int:

    """
            Donne la valeur de const.VISIBLE dans la cellule

            :param cell : variable qui représente une case


            :return: la valeur de const.VISIBLE d'une case
    """

    return cell[const.VISIBLE]


def setContenuCellule(cell: dict, contenu: int) -> None:

    """
            Permet de changer le contenu d'une cellule

            :param cell : variable qui représente une case
                   contenu : variable qui représente le nombre de mine autour de cette case / VALEUR PAR DEFAUT = 0


            :return: rien
    """

    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")

    if isContenuCorrect(contenu) == False:
        raise ValueError("setContenuCellule : la valeur du contenu", contenu, " n’est pas correcte.")

    if type_cellule(cell) == False:
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")

    if contenu == -1 :
        contenu = const.ID_MINE

    cell[const.CONTENU] = contenu

    return None


def setVisibleCellule(cell: dict, visibilite: bool) -> None:

    """
            Permet de changer la visibilité d'une cellule

            :param cell : variable qui représente une case
                   visible: variable qui représente si la case est visible ou non (True si oui, False sinon)


            :return: rien
    """

    if type_cellule(cell) == False:
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visibilite) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")

    cell.update({const.VISIBLE: visibilite})

    return None


def contientMineCellule(cell: dict) -> bool:

    """
            Permet de savoir si une cellule contient une mine ou non (True si oui, False sinon)

            :param cell : variable qui représente une case


            :return: True/False selon si la case contient une mine ou non
    """

    contientMineBool = False

    if cell[const.CONTENU] == const.ID_MINE:
        contientMineBool = True

    return contientMineBool


def isAnnotationCorrecte(annotation : str) -> bool :

    """
            Permet de vérifier si l'annotation est correcte(None/const.FLAG/const.DOUTE)

            :param annotation : variable qui représente l'annotation présente sur la case


            :return: True/False selon si l'annotation est correcte ou non
    """

    isAnnotationCorrecteBool = False

    if annotation == const.DOUTE or annotation == const.FLAG or annotation == None :
        isAnnotationCorrecteBool = True

    return isAnnotationCorrecteBool


def getAnnotationCellule(cell: dict) -> str :

    """
            Permet de récupérer l'annotation d'une cellule

            :param annotation : variable qui représente l'annotation présente sur la case


            :return: l'annotation correspondant à la cellule
    """

    if type_cellule(cell) == False :
        raise TypeError("getAnnotationCellule : le paramètre", cell ," n’est pas une cellule")

    if const.ANNOTATION not in cell :
        return None

    return cell[const.ANNOTATION]


def changeAnnotationCellule(cell : dict):

    """
            Permet de changer l'annotation d'une cellule (None/const.FLAG/const.DOUTE)

            :param cell : variable qui représente une case


            :return: rien
    """

    if type_cellule(cell) == False :
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")


    if cell[const.ANNOTATION] ==  const.FLAG:
            cell[const.ANNOTATION] = const.DOUTE
            return

    if cell[const.ANNOTATION] == None :
            cell[const.ANNOTATION] =  const.FLAG
            return

    if cell[const.ANNOTATION] == const.DOUTE:
            cell[const.ANNOTATION] = None
            return



    return


def reinitialiserCellule(cell : dict):

    """
            Permet de  renitialiser la cellule (mettre tous ses paramètres à défaut)

            :param cell : variable qui représente une case


            :return: rien
    """

    return cell.update({const.VISIBLE: False}),cell.update({const.CONTENU: 0}),cell.update({const.ANNOTATION: None})


