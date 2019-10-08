################################################################################
###                   Test des commandes PRENDRE et POSER                    ###
################################################################################
###                                 Syntaxe                                  ###
###--------------------------------------------------------------------------###
### PRENDRE motCleObj                                                        ###
### POSER motCleObj                                                          ###
###                                                                          ###
### Le module met l'instruction en minuscule, donc la casse n'influe pas sur ###
### la capacité du programme à interpréter la commande.                      ###
###                                                                          ###
### Les mots-clés sont donnés à titre d'exemple. L'utilisation d'une classe  ###
### Item permet de faciliter à long terme la gestion de l'inventaire joueur  ###
### ainsi que l'appel à la commande UTILISER.                                ###
###                                                                          ###
###     IDÉE POUR PLUS TARD N°1 - IMPLÉMENTER SOL COMME PARAMÈTRE DE SALLE   ###
### Les seuls objets dont la présence doit être conservée d'une salle à une  ###
### autre sont ceux stockés dans l'inventaire. Cependant, il faut quand même ###
### que les objets laissés au sol ne soient pas effacés lorsqu'on change de  ###
### pièce. Ainsi, pour conserver cette permanence, on pourrait implémenter   ###
### la liste des objets au sol comme paramètre d'une salle en plus de ses    ###
### quatre attributs existants (voir testALLER.py).                          ###
################################################################################

class Item :
    def __init__(self, name, inInventory) :
        self.name = name
        self.inInventory = inInventory

pelle = Item("Pelle", False)
carte = Item("Carte", False)
torche = Item("Torche", True)

objets = [pelle, carte, torche]

commande = ""
commForm = []

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

while not("exit" in commForm) :
    print("Dans la salle se trouve :\n")
    for item in objets :
        if not(item.inInventory) :
            print(item.name + "\n")
    print("Vous avez sur vous :\n")
    for item in objets :
        if item.inInventory :
            print(item.name + "\n")
    commande = input("Entrez PRENDRE ou POSER suivi du nom de l'objet s'il l'ajouter ou le retirer de votre inventaire.")
    commForm = commande.lower().split()
    inventory = inventaire(objets)
    ground = priveDe(objets, inventory)
    if "prendre" in commForm :
        for item in ground :
            if (item.name.lower() in commForm) :
                item.inInventory = True
    elif "poser" in commForm :
        for item in inventory :
            if(item.name.lower() in commForm) :
                item.inInventory = False
    elif not("exit" in commForm) :
        print("You talkin' to me ?")