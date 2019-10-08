################################################################################
###                       Test de la commande OBSERVER                       ###
################################################################################
###                                 Syntaxe                                  ###
###--------------------------------------------------------------------------###
### OBSERVER motCleObjet                                                     ###
###                                                                          ###
### Le module met l'instruction en minuscule, donc la casse n'influe pas sur ###
### la capacité du programme à interpréter la commande.                      ###
###                                                                          ###
###     CONTRAINTE N°1 - STOCKAGE DES DESCRIPTIONS                           ###
### Les descriptions sont, par définition, longues et précises. Lorsqu'on a  ###
### peu d'objets pouvant être décrits, comme ici où l'on en a seulement un,  ###
### on peut se permettre de les implémenter dans le code. Cependant, si l'on ###
### a beaucoup d'objets, il faudra envisager de les stocker ailleurs que sur ###
### le programme, par exemple dans des documents texte à part.               ###
################################################################################

class Item :
    def __init__(self, name, canBeObserved, desc) :
        self.name = name
        self.canBeObserved = canBeObserved
        self.desc = desc

pelle = Item("Pelle", True, "Une pelle. Un outil fort pratique. Celle-là est faite d'un manche en chêne massif et d'une tête en fer. Malgré quelques entailles çà et là, le manche est en bon état, conservant sa forme et sa longueur initiales ainsi que son vernis d'origine. La tête, quant à elle, n'a pas eu autant de chance. Elle semble avoir été dévorée par la rouille un peu partout. Des taches de terre, sable et... du sang, probablement, sont également incrustées. À en juger par l'usure inégale sur les deux tranches et la répartition des taches poupres, on peut supposer que cette pelle n'a pas servi qu'à creuser dans un matériau meuble.")

commande = ""
commForm = []

while not("exit" in commForm) :
    commande = input("Entrez OBSERVER suivi du nom d'un objet.")
    commForm = commande.lower().split()
    if pelle.name.lower() in commForm :
        print(pelle.desc)