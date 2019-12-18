from random import shuffle
import classes
import labyrinthe_aleatoire as mazeGen
from sousFonctions import recupDesc

#################################################################################################################################
# Déclaration des variables liées au labyrinthe
### \/ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES \/ ###
ligne = 7
colonne = 7
### /\ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES /\ ###

ligneFin = ((ligne - 1)//2)
colFin = ((colonne - 1)//2)

freedom = classes.Final()

# Importation des descriptions de salle
arm = recupDesc("salle-armurerie")
bib = recupDesc("salle-bibliotheque")
c11e = recupDesc("salle-chambre1x1E")
c12a = recupDesc("salle-chambre1x2A")
coul2a = recupDesc("salle-couloir2Angle")
coul2d = recupDesc("salle-couloir2Droit")
coul3 = recupDesc("salle-couloir3")
coul4 = recupDesc("salle-couloir4")
cuis = recupDesc("salle-cuisine")
deb = recupDesc("salle-debarras")

#################################################################################################################################
# Génération du labyrinthe
### Étape 1 - Génération d'un labyrinthe vide aux dimensions finales
maze = [[None] * colFin] * ligneFin

### Étape 2 - Génération d'un labyrinthe "surdimensionné"
laby = mazeGen.labyrinthe_aleatoire(ligne,colonne)

### Étape 3 - Convertir le labyrinthe surdimensionné (tableau de booléens) en labyrinthe interprétable (tableau de Salles)
doors = mazeGen.passages(laby[0])

### Étape 4 - On déclare tous les objets à utiliser
seau = classes.Item("Seau d'eau", False, True, 1, True, False)
pelle = classes.Item("Pelle", False, True, -1, False, True, recupDesc("item-pelle"))
bouclier = classes.Item("Bouclier", False, True, 1, False, True, recupDesc("item-bouclier"))
grosseCle = classes.Item("Grosse clé", False, True, 1, False, True, recupDesc("item-grosseCle"))

items = [seau, pelle, bouclier, grosseCle]

### Étape 5 - On déclare tous les mécanismes qui seront ajoutés
feu = classes.Mecanism("Feu", seau, pelle, True, recupDesc("meca-feu"), recupDesc("meca-feu-res"))
sable = classes.Mecanism("Tas de sable", pelle, bouclier, True, recupDesc("meca-sable"), recupDesc("meca-sable-res"))
armure = classes.Mecanism("Armure", bouclier, grosseCle, True, recupDesc("meca-armure"), recupDesc("meca-armure-res"))
porte = classes.Mecanism("Grosse porte", grosseCle, freedom, True, recupDesc("meca-porte"), recupDesc("meca-porte-res"))

mecas = [seau, feu, sable, armure, porte]

### Étape 6 - Positionnement des objets et mécanismes
nb_pos = len(mecas)

### Étape 7 - Association des positions et objets
#### 71 - Placement des mécanismes dans le labyrinthe
choix = mazeGen.mecanisme(laby, nb_pos)

#### 72 - Liste des abscisses et liste des ordonnées des salles avec mécanismes dans le labyrinthe final
meca_x=[]
meca_y=[]
for i in range(len(choix)):
    meca_x.append((laby[1][i] - 1) // 2)
    meca_y.append((laby[2][i] - 1) // 2)

#### 73 - Intégration des mécanismes utiles dans les salles concernées
labItems = []
labMeca = []

for i in range(ligneFin) :
    ligneTempMeca = []
    ligneTempItem = []
    for j in range(colFin) :
        caseTempMeca = []
        caseTempItem = []
        for k in range(len(choix)):
            if i == meca_x[k] and j == meca_y[k] :
                if type(mecas[k]) == classes.Item :
                    caseTempItem.append(mecas[k])
                elif type(mecas[k]) == classes.Mecanism :
                    caseTempMeca.append(mecas[k])
                    caseTempItem.append(mecas[k].objFin)
        ligneTempMeca.append(caseTempMeca)
        ligneTempItem.append(caseTempItem)
    labMeca.append(ligneTempMeca)
    labItems.append(ligneTempItem)

### Étape 8 - Donner une description à chaque salle
descSalles = [arm, bib, c11e, c12a, cuis, deb]
shuffle(descSalles)
labDesc = []

for li in range(ligneFin) :
    tabTemp = []
    for col in range(colFin) :
        nbPortes = int(doors[li][col]["nord"]) + int(doors[li][col]["est"]) + int(doors[li][col]["sud"]) + int(doors[li][col]["ouest"])
        if nbPortes == 1 :
            tabTemp.append(descSalles[0])
            del(descSalles[0])
        elif nbPortes == 2 :
            tabTemp.append(coul2d if doors[li][col]["nord"] == doors[li][col]["sud"] else coul2a)
        elif nbPortes == 3 :
            tabTemp.append(coul3)
        elif nbPortes == 4 :
            tabTemp.append(coul4)
    labDesc.append(tabTemp)

### Étape finale - Tout est prêt, il n'y a plus qu'à construire le labyrinthe
maze = [[classes.Salle(doors[i][j]["nord"], doors[i][j]["est"], doors[i][j]["sud"], doors[i][j]["ouest"], labItems[i][j], labMeca[i][j], labDesc[i][j]) for j in range(colFin)] for i in range(ligneFin)]