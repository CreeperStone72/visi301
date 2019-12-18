def recupDesc(objet) :
    """Retourne la description d'un objet donné

    Input : objet, une chaîne de caractères
    Output : desc, une chaîne de caractères"""
    fichier = open("descriptions/"+objet+".txt", 'r', encoding="utf-8")
    desc = fichier.read()
    fichier.close()
    return desc

from random import shuffle
import genMaze
import classes

def inventaire(obj) :
    """Trie les éléments d'un objet et retourne une liste des objets contenus dans l'inventaire

    Input : obj, une liste d'Items
    Output : inventory, une liste d'Items"""
    inventory = []
    for objet in obj :
        if objet.inInventory :
            inventory.append(objet)
    return inventory

def priveDe(A, B) :
    """Permet de déterminer A\B, A et B étant ici deux listes données telles que B est inclus dans A

    Input : A, une liste
            B, une liste
    Output : ground, une liste"""
    ground = []
    for objet in A :
        if not(objet in B) :
            ground.append(objet)
    return ground

def subset(liste1, liste2) :
    """Permet de savoir si une liste est un sous-ensemble d'une autre

    Input : liste1, une liste
            liste2, une liste
    Output : included, un booléen"""
    listeTemp = [el for el in liste1]
    cpt = 0
    for el in liste2 :
        if listeTemp[0] == el :
            cpt += 1
            del(listeTemp[0])
        if len(listeTemp) == 0 :
            break
    return cpt == len(liste1)

def affiche_inventaire() :
    """Retourne l'inventaire joueur

    Output : inventory, une chaîne de caractères"""
    objets = inventaire(genMaze.items)
    inventory = ""
    if len(objets) > 0 :
        inventory = "Vous avez sur vous : " + ", ".join([item.name for item in objets])
    else :
        inventory = "Vous n'avez que vos habits"
    inventory += "."
    return inventory

def affiche_objets(salle) :
    """Retourne les Item et Mecanism présent dans une salle

    Input : salle, une Salle
    Output : objets, une chaîne de caractères"""
    listTotal = []

    for item in salle.objets :
        if item.exists and (type(item) != classes.Final and not(item.inInventory)) :
            listTotal.append(item)
    for meca in salle.mecas :
        if meca.exists :
            listTotal.append(meca)
    shuffle(listTotal)
    listeObjets = []
    cptAff = 0
    for el in listTotal :
        listeObjets.append(el.name)
        cptAff += 1

    objets = ""
    if cptAff > 0 :
        if cptAff == 1 :
            objets = "Est présent " + listeObjets[0]
        else :
            objets = "Sont présents " + ", ".join(listeObjets)
    else :
        objets = "Rien d'intérêt présent ici"
    objets += "."
    return objets

def affiche_portes(salle) :
    """Retourne les portes praticables par le joueur

    Input : salle, une Salle
    Output : portes, une chaîne de caractères"""
    nbPortes = int(salle.porteN) + int(salle.porteE) + int(salle.porteS) + int(salle.porteO)
    portes = "Est présente " if nbPortes == 1 else "Sont présentes "
    portes += ("une porte au nord" + (", " if (salle.porteE or salle.porteS or salle.porteO) else " ")) if salle.porteN else ""
    portes += ("une porte à l'est" + (", " if (salle.porteS or salle.porteO) else " ")) if salle.porteE else ""
    portes += ("une porte au sud" + (", " if salle.porteO else " ")) if salle.porteS else ""
    portes += "une porte à l'ouest" if salle.porteO else ""
    portes += "."
    return portes