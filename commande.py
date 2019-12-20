from classes import *
import genMaze
import sousFonctions as subFc

# Note : La plupart des commandes retournent la chaîne de caractères erreur en cas d'action incorrecte

def aller(direction, xForm, yForm) :
    """Se déplace dans une salle adjacente si possible

    Input : direction, une chaîne de caractères
            xForm, un entier
            yForm, un entier
    Output : coordFin, une paire d'entiers"""
    erreur = ""
    if (direction == "nord") and genMaze.maze[xForm][yForm].porteN :
        xForm -= 1
    elif (direction == "est") and genMaze.maze[xForm][yForm].porteE :
        yForm += 1
    elif (direction == "sud") and genMaze.maze[xForm][yForm].porteS :
        xForm += 1
    elif (direction == "ouest") and genMaze.maze[xForm][yForm].porteO :
        yForm -= 1
    else :
        erreur = "Ouch ! Comment j'ai pu ne pas voir qu'il y avait un mur ?"
    return [xForm, yForm], erreur

def prendre_poser(objet, xForm, yForm, prendre) :
    """Prend ou pose un objet, selon qu'il soit dans l'inventaire ou non

    Input : objet, une chaîne de caractères
            xForm, un entier
            yForm, un entier
            prendre, un booléen"""
    inv = subFc.inventaire(genMaze.items)
    ground = subFc.priveDe(genMaze.maze[xForm][yForm].objets, inv)
    if prendre :
        for item in range(len(ground)) :
            if ground[item].name.lower() == objet and ground[item].exists :
                ground[item].inInventory = True
                del(genMaze.maze[xForm][yForm].objets[item])
    else :
        for item in inv :
            if item.name.lower() == objet :
                item.inInventory = False
                if not(item in ground) :
                    genMaze.maze[xForm][yForm].objets.append(item)


def utiliser(objets, xForm, yForm) :
    """Utilise l'objet sur le mécanisme

    Input : objets, une chaîne de caractères
            xForm, un entier
            yForm, un entier
    Output : res, une chaîne de caractères"""
    res = ""
    erreur = ""
    inv = subFc.inventaire(genMaze.items)
    for item in inv :
        for meca in genMaze.maze[xForm][yForm].mecas :
            if (subFc.subset(item.name.lower().split(), objets) and item.exists) and (subFc.subset(meca.name.lower().split(), objets) and meca.exists) :
                if meca.objInteract == item :
                    item.uses -= 1
                    if item.uses == 0 :
                        item.exists = False
                        item.inInventory = False
                    meca.exists = False
                    meca.objFin.exists = True
                    res = meca.descRes
                    if type(meca.objFin) == Transport :
                        meca.objFin.ouverture()
                else :
                    erreur = "Huh, on dirait que ça ne sert pas pour ça..."
    return res, erreur

def observer(objet, xForm, yForm) :
    """Affiche la description d'un objet

    Input : objet, une chaîne de caractères
    Output : res, une chaîne de caractères
             erreur, une chaîne de caractères"""
    res = ""
    erreur = "Je ne sais pas quoi dire..."
    inv = subFc.inventaire(genMaze.items)
    for item in inv :
        if (item.name.lower() == objet) and (item.canBeObserved) :
            res = item.desc
            erreur = ""
    for meca in genMaze.maze[xForm][yForm].mecas :
        if (meca.name.lower() == objet) :
            res = meca.desc
            erreur = ""
    return res, erreur