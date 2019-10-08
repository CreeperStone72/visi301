################################################################################
###                        Test de la commande ALLER                         ###
################################################################################
###                                 Syntaxe                                  ###
###--------------------------------------------------------------------------###
### ALLER motCleDirection                                                    ###
###                                                                          ###
### Le module met l'instruction en minuscule, la casse n'influe donc pas sur ###
### la capacité du programme à comprendre la commande.                       ###
###                                                                          ###
### Ici, les mots clés de direction sont les quatre points cardinaux. Il est ###
### toutefois possible de modifier ces mots clés à discrétion.               ###
###                                                                          ###
###     CONTRAINTE N°1 - FORMAT DU LABYRINTHE                                ###
### Pour que la commande fonctionne correctement, il faut que le labyrinthe  ###
### soit une liste de liste de Salles, Salle étant une classe possédant 4    ###
### paramètres booléens indiquant s'il y a une porte au nord/sud/est/ouest.  ###
################################################################################

# Création d'un labyrinthe
class Salle :
    def __init__(self, porteN, porteE, porteS, porteO) :
        self.porteN = porteN
        self.porteE = porteE
        self.porteS = porteS
        self.porteO = porteO

salle00 = Salle(True, True, False, False)
salle01 = Salle(False, False, True, True)
salle02 = Salle(False, False, True, False)

salle10 = Salle(False, False, True, False)
salle11 = Salle(True, True, False, False)
salle12 = Salle(True, False, True, True)

salle20 = Salle(True, True, False, False)
salle21 = Salle(False, True, False, True)
salle22 = Salle(True, False, False, True)

salle00.porteN = False

maze = [[salle00, salle01, salle02],[salle10, salle11, salle12],[salle20, salle21, salle22]]

# Obtention et formatage de la commande

currentX = 2
currentY = 1

while not(currentX == 0 and currentY == 0) :
    print("Salle actuelle :",currentX,currentY)
    commande = input("Entrez une commande commençant par Aller et suivie d'un des quatre points cardinaux")
    commForm = commande.lower().split()
    if "aller" in commForm :
        if ("nord" in commForm) and maze[currentX][currentY].porteN :
            currentX -= 1
        elif ("est" in commForm) and maze[currentX][currentY].porteE :
            currentY += 1
        elif ("sud" in commForm) and maze[currentX][currentY].porteS :
            currentX += 1
        elif ("ouest" in commForm) and maze[currentX][currentY].porteO :
            currentY -= 1
        else :
            print("I'm sorry Dave. I'm afraid I can't let you do that.")
    else :
        print("You talkin' to me ?")
print("Okay, here’s the story. I come from the gutter. I know that. I got no education but that’s okay. I know the street, and I’m making all the right connections. With the right woman, there’s no stopping me. I could go right to the top.")