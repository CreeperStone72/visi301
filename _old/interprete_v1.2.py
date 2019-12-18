# Déclaration des classes

class Item :
    def __init__(self, name, inInventory, usable, exists, canBeObserved, desc = "") :
        self.name = name
        self.inInventory = inInventory
        self.usable = usable
        self.exists = exists
        self.canBeObserved = canBeObserved
        self.desc = desc

class Mecanism :
    def __init__(self, name, objInteract, objFin, exists) :
        self.name = name
        self.objInteract = objInteract
        self.objFin = objFin
        self.exists = exists

class Transport :
    def __init__ (self, salle, pointCard, exists) :
        self.salle = salle
        self.pointCard = pointCard
        self.exists = exists
    def ouverture(self) :
        if self.pointCard == "Nord" :
            self.salle.porteN = True
        elif self.pointCard == "Est" :
            self.salle.porteE = True
        elif self.pointCard == "Sud" :
            self.salle.porteS = True
        elif self.pointCard == "Ouest" :
            self.salle.porteO = True

class Salle :
    def __init__(self, porteN, porteE, porteS, porteO, objets, mecas) :
        self.porteN = porteN
        self.porteE = porteE
        self.porteS = porteS
        self.porteO = porteO
        self.objets = objets
        self.mecas = mecas

# Déclaration des objets de test et des variables globales

pelle = Item("Pelle", False, False, True, True, "Une pelle. Un outil fort pratique. Celle-là est faite d'un manche en chêne massif et d'une tête en fer. Malgré quelques entailles çà et là, le manche est en bon état, conservant sa forme et sa longueur initiales ainsi que son vernis d'origine. La tête, quant à elle, n'a pas eu autant de chance. Elle semble avoir été dévorée par la rouille un peu partout. Des taches de terre, sable et... du sang, probablement, sont également incrustées. À en juger par l'usure inégale sur les deux tranches et la répartition des taches poupres, on peut supposer que cette pelle n'a pas servi qu'à creuser dans un matériau meuble.")
clePorte = Item("Clé", False, True, False, True, "Une grosse clé. Elle a l'air d'ouvrir quelque chose d'important...")

salle00 = Salle(False, False, True, False, [], [])
salle01 = Salle(False, False, True, False, [clePorte], [])

salle10 = Salle(True, True, False, False, [pelle], [])
salle11 = Salle(True, False, False, True, [], [])

maze = [[salle00, salle01],[salle10, salle11]]

porte00N = Transport(salle00, "Nord", False)

tasDeSable = Mecanism("Sable", pelle, clePorte, True)
porteFermee = Mecanism("Porte", clePorte, porte00N, True)

salle00.mecas = [porteFermee]
salle01.mecas = [tasDeSable]

objets = [pelle, clePorte]
mecanismes = [tasDeSable,porteFermee]

currentX = 1
currentY = 1

commande = ""
commForm = ["",""]

# Déclaration des fonctions de commande

def aller(direction, xForm, yForm) :
    """Se déplace dans une salle adjacente si possible"""
    if (direction == "nord") and maze[xForm][yForm].porteN :
        xForm -= 1
    elif (direction == "est") and maze[xForm][yForm].porteE :
        yForm += 1
    elif (direction == "sud") and maze[xForm][yForm].porteS :
        xForm += 1
    elif (direction == "ouest") and maze[xForm][yForm].porteO :
        yForm -= 1
    else :
        print("Ouch ! Comment j'ai pu ne pas voir qu'il y avait un mur ?")
    return [xForm, yForm]

def prendre_poser(objet, xForm, yForm) :
    """Prend ou pose un objet, selon qu'il soit dans l'inventaire ou non"""
    if "prendre" in commForm :
        for item in ground :
            if item == objet :
                item.inInventory = True
    elif "poser" in commForm :
        for item in inventory :
            if item == objet :
                item.inInventory = False
                maze[xForm][yForm].objets.append(objet)


def utiliser(objet, mecanisme) :
    """Utilise l'objet sur le mécanisme"""
    if mecanisme.objInteract == objet :
        objet.exists = False
        mecanisme.exists = False
        mecanisme.objFin.exists = True
        if type(mecanisme.objFin) == Transport :
            mecanisme.objFin.ouverture()

def observer(objet) :
    """Affiche la description d'un objet"""
    for item in inventory :
        if (item == objet) and (item.canBeObserved) :
            print(item.desc)

# Déclaration des sous-fonctions

def formatage(comm) :
    """Formate une commande afin de retourner un tableau exploitable

    Input : comm, une chaîne de caractères
    Output : formatted, une liste de chaînes de caractères"""
    formatted = comm.lower().split()
    if formatted[0] == "utiliser" :
        formatted = formatted[0:3]
    else :
        formatted = formatted[0:2]
    return formatted

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

    Input : A, une liste d'Items
            B, une liste d'Items
    Output : ground, une liste d'Items"""
    ground = []
    for objet in A :
        if not(objet in B) :
            ground.append(objet)
    return ground

def affiche_items(objects) :
    """Affiche en liste verticale tous les items présents dans une liste donnée

    Input : objects, une liste d'items
    Output : affichage, une chaîne de caractères"""
    affichage = ""
    for item in objects :
        if item.exists :
            affichage += item.name + "\n"
    return affichage

def affiche_mecanismes(mecas) :
    """Affiche en liste verticale tous les mécanismes présents dans une liste donnée

    Input : mecas, une liste de mécanismes
    Output : affichage, une chaîne de caractères"""
    affichage = ""
    for mecanisme in mecas :
        if mecanisme.exists :
            affichage += mecanisme.name + "\n"
    return affichage

def id_name_item(nom) :
    """Retourne l'item associé à son attribut nom

    Input : nom, une chaîne de caractères
    Output : objet, un item"""
    objet = None
    for item in objets :
        if item.name.lower() == nom :
            objet = item
    return objet

def id_name_meca(nom) :
    """Retourne le mécanisme associé à son attribut nom

    Input : nom, une chaîne de caractères
    Output : objet, un mécanisme"""
    objet = None
    for mecanisme in mecanismes :
        if mecanisme.name.lower() == nom :
            objet = mecanisme
    return objet

# Corps du programme

while not(salle00.porteN) :
    # Interprétation de la commande actuelle
    if commForm[0] == "aller" :
        salleNext = aller(commForm[1], currentX, currentY)
        currentX = salleNext[0]
        currentY = salleNext[1]
    else :
        objet = id_name_item(commForm[1])
        if commForm[0] in ["prendre", "poser"] :
            prendre_poser(objet, currentX, currentY)
        elif commForm[0] == "utiliser" :
            meca = id_name_meca(commForm[2])
            utiliser(objet, meca)
        elif commForm[0] == "observer" :
            observer(objet)
    # Génération des listes variables d'objets
    inventory = inventaire(objets)
    ground = priveDe(maze[currentX][currentY].objets, inventory)
    # Affichage de la position
    print("Salle actuelle :",currentX,currentY,"\n")
    # Affichage des localisations d'objets
    print("Se trouvent par terre :\n" + affiche_items(ground))
    print("Mécanismes présents :\n" + affiche_mecanismes(maze[currentX][currentY].mecas))
    print("Vous avez dans votre inventaire :\n" + affiche_items(inventory))
    # Obtention de l'instruction suivante
    commande = input("Entrez l'une des commandes suivie du nom d'un objet et éventuellement d'un mécanisme s'il s'agit d'UTILISER")
    commForm = formatage(commande)
