################################################################################
###                       Test de la commande UTILISER                       ###
################################################################################
###                                 Syntaxe                                  ###
###--------------------------------------------------------------------------###
### UTILISER motCleItem motCleMecanism                                       ###
###                                                                          ###
### Le module met l'instruction en minuscule, donc la casse n'influe pas sur ###
### la capacité du programme à interpréter la commande.                      ###
###                                                                          ###
### Les mots-clés sont donnés à titre d'exemple. On réutilise ici la classe  ###
### Item qui avait été créée pour le test des commandes PRENDRE et POSER     ###
### (voir testPRENDRE-POSER.py).                                             ###
###                                                                          ###
###     MARGE DE MANŒUVRE N°1 - LAXISME DE PYTHON SUR LES TYPES              ###
### Comme Python est assez... souple, disons, sur le type des variables, il  ###
### est tout à fait possible que sur deux objets Mecanism, leurs propriétés  ###
### .objInteract et .objFin respectives ne soient pas du même type.          ###
### Par exemple, ici, on utilise la clé sur le coffre pour obtenir la carte  ###
### (Item + Mecanism = Item). Cependant, une clé pourrait aussi ouvrir une   ###
### porte verrouillée (Item + Mecanism = Transport).                         ###
### Par conséquent, on peut avoir plus de liberté quant au type Mecanism que ###
### l'on ne pourrait pas avoir dans d'autres langages de programmation.      ###
################################################################################

class Item :
    def __init__(self, name, usable, exists) :
        self.name = name
        self.usable = usable
        self.exists = exists

class Mecanism :
    def __init__(self, name, objInteract, objFin, exists) :
        self.name = name
        self.objInteract = objInteract
        self.objFin = objFin
        self.exists = exists

cle = Item("Clé", False, True)
carte = Item("Carte", False, False)

objets = [cle, carte]

coffre = Mecanism("Coffre", cle, carte, True)

while not(carte.exists) :
    print("Items présents\n")
    for item in objets :
        if item.exists :
            print(item.name + "\n")
    print("Mécanismes présents\n")
    if coffre.exists :
        print(coffre.name + "\n")
    commande = input("Entrez UTILISER suivi d'un item et d'un mécanisme")
    commForm = commande.lower().split()
    if "utiliser" in commForm :
        if cle.name.lower() in commForm and coffre.name.lower() in commForm :
            coffre.exists = False
            cle.exists = False
            carte.exists = True
    else :
        print("Say that again ?")
print("Vous avez trouvé une carte du donjon !")