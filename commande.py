from classes import *
import genMaze

def aller(direction, xForm, yForm) :
    """Se déplace dans une salle adjacente si possible

    Input : direction, une chaîne de caractères
            xForm, un entier
            yForm, un entier
    Output : coordFin, une paire d'entiers"""
    if (direction == "nord") and genMaze.maze[xForm][yForm].porteN :
        xForm -= 1
    elif (direction == "est") and genMaze.maze[xForm][yForm].porteE :
        yForm += 1
    elif (direction == "sud") and genMaze.maze[xForm][yForm].porteS :
        xForm += 1
    elif (direction == "ouest") and genMaze.maze[xForm][yForm].porteO :
        yForm -= 1
    else :
        ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
        print("Ouch ! Comment j'ai pu ne pas voir qu'il y avait un mur ?")
    return [xForm, yForm]

def prendre_poser(objet, xForm, yForm, prendre) :
    """Prend ou pose un objet, selon qu'il soit dans l'inventaire ou non

    Input : objet, un Item
            xForm, un entier
            yForm, un entier
            prendre, un booléen"""
    if prendre :
        for item in ground :
            if item == objet :
                if item.inInventory :
                    ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
                    print("Tiens ? C'est vrai que je l'ai déjà ramassé.")
                else :
                    item.inInventory = True
    else :
        for item in inventory :
            if item == objet :
                if not(item.inInventory) :
                    ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
                    print("Mais... Il est déjà posé.")
                else :
                    item.inInventory = False
                if not(item in genMaze.maze[xForm][yForm].objets) :
                    genMaze.maze[xForm][yForm].objets.append(item)


def utiliser(objet, mecanisme) :
    """Utilise l'objet sur le mécanisme

    Input : objet, un Item
            mecanisme, un Mecanism"""
    if mecanisme.objInteract == objet :
        objet.uses -= 1
        if objet.uses == 0 :
            objet.exists = False
        mecanisme.exists = False
        mecanisme.objFin.exists = True
        if type(mecanisme.objFin) == Transport :
            mecanisme.objFin.ouverture()
        ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
        print(mecanisme.descRes)
    else :
        ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
        print("Huh, on dirait que ça ne sert pas pour ça...")

def observer(objet) :
    """Affiche la description d'un objet"""
    for item in inventory :
        if (item == objet) and (item.canBeObserved) :
            ### MODIFIER L'AFFICHAGE DU MESSAGE APRÈS CHANGEMENT D'INTERFACE
            print(item.desc)