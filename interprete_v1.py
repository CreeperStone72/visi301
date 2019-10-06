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

# Déclaration des objets de test et des variables globales

pelle = Item("Pelle", False, False, True, True, "Une pelle. Un outil fort pratique. Celle-là est faite d'un manche en chêne massif et d'une tête en fer. Malgré quelques entailles çà et là, le manche est en bon état, conservant sa forme et sa longueur initiales ainsi que son vernis d'origine. La tête, quant à elle, n'a pas eu autant de chance. Elle semble avoir été dévorée par la rouille un peu partout. Des taches de terre, sable et... du sang, probablement, sont également incrustées. À en juger par l'usure inégale sur les deux tranches et la répartition des taches poupres, on peut supposer que cette pelle n'a pas servi qu'à creuser dans un matériau meuble.")
carte = Item("Carte", False, False, False, False)
torche = Item("Torche", True, False, True, False)
cle = Item("Clé", True, True, True, False)
carte = Item("Carte", False, False, False, False)

coffre = Mecanism("Coffre", cle, carte, True)

objets = [pelle, carte, torche, cle, carte]
mecanismes = [coffre]

commande = ""
commForm = ["",""]

# Déclaration des fonctions de commande

def prendre_poser(objet) :
    """Prend ou pose un objet, selon qu'il soit dans l'inventaire ou non"""
    if "prendre" in commForm :
        for item in ground :
            if item == objet :
                item.inInventory = True
    elif "poser" in commForm :
        for item in inventory :
            if item == objet :
                item.inInventory = False

def utiliser(objet, mecanisme) :
    """Utilise l'objet sur le mécanisme"""
    if mecanisme.objInteract == objet :
        objet.exists = False
        mecanisme.exists = False
        mecanisme.objFin.exists = True

def observer(objet) :
    """Affiche la description d'un objet"""
    for item in inventory :
        if (item == objet) and (item.canBeObserved) :
            print(pelle.desc)

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
    for item in objets :
        if item.name.lower() == nom :
            objet = item
    return item

def id_name_meca(nom) :
    """Retourne le mécanisme associé à son attribut nom

    Input : nom, une chaîne de caractères
    Output : objet, un mécanisme"""
    for mecanisme in mecanismes :
        if mecanisme.name.lower() == nom :
            objet = mecanisme
    return mecanisme

# Corps du programme

while not("exit" in commForm) :
    # Interprétation de la commande actuelle
    objet = id_name_item(commForm[1])
    if commForm[0] in ["prendre", "poser"] :
        prendre_poser(objet)
    elif commForm[0] == "utiliser" :
        meca = id_name_meca(commForm[2])
        utiliser(objet, meca)
    elif commForm[0] == "observer" :
        observer(objet)
    # Génération des listes variables d'objets
    inventory = inventaire(objets)
    ground = priveDe(objets, inventory)
    # Affichage des localisations d'objets
    print("Se trouvent par terre :\n" + affiche_items(ground))
    print("Mécanismes présents :\n" + affiche_mecanismes(mecanismes))
    print("Vous avez dans votre inventaire :\n" + affiche_items(inventory))
    # Obtention de l'instruction suivante
    commande = input("Entrez l'une des commandes suivie du nom d'un objet et éventuellement d'un mécanisme s'il s'agit d'UTILISER")
    commForm = formatage(commande)