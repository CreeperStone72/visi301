### MODIFIER CETTE FONCTION - IMPORTANT
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

### MODIFIER CETTE FONCTION APRÈS CHANGEMENT D'INTERFACE
def affiche_items(objects) :
    """Affiche en liste verticale tous les items présents dans une liste donnée

    Input : objects, une liste d'items
    Output : affichage, une chaîne de caractères"""
    affichage = ""
    for item in objects :
        if item.exists :
            affichage += item.name + "\n"
    return affichage

### MODIFIER CETTE FONCTION APRÈS CHANGEMENT D'INTERFACE
def affiche_mecanismes(mecas) :
    """Affiche en liste verticale tous les mécanismes présents dans une liste donnée

    Input : mecas, une liste de mécanismes
    Output : affichage, une chaîne de caractères"""
    affichage = ""
    for mecanisme in mecas :
        if mecanisme.exists :
            affichage += mecanisme.name + "\n"
    return affichage

### MODIFIER CETTE FONCTION - URGENT
def id_name_item(nom) :
    """Retourne l'item associé à son attribut nom

    Input : nom, une chaîne de caractères
    Output : objet, un item"""
    objet = None
    for item in objets :
        if item.name.lower() == nom :
            objet = item
    return objet

### MODIFIER CETTE FONCTION - URGENT
def id_name_meca(nom) :
    """Retourne le mécanisme associé à son attribut nom

    Input : nom, une chaîne de caractères
    Output : objet, un mécanisme"""
    objet = None
    for mecanisme in mecanismes :
        if mecanisme.name.lower() == nom :
            objet = mecanisme
    return objet

def recupDesc(objet) :
    """Retourne la description d'un objet donné

    Input : objet, une chaîne de caractères
    Output : desc, une chaîne de caractères"""
    fichier = open("descriptions/"+objet+".txt", 'r', encoding="utf-8")
    desc = fichier.read()
    fichier.close()
    return desc