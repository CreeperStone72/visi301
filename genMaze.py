import classes
import labyrinthe_aleatoire as mazeGen

#################################################################################################################################
# Déclaration des variables liées au labyrinthe
### \/ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES \/ ###
ligne = 7
colonne = 7
### /\ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES /\ ###

ligneFin = ((ligne - 1)//2)
colFin = ((colonne - 1)//2)

#################################################################################################################################
# Génération du labyrinthe
### Étape 1 - Génération d'un labyrinthe vide aux dimensions finales
maze = [[classes.Salle()] * colFin] * ligneFin

### Étape 2 - Génération d'un labyrinthe "surdimensionné"
laby = mazeGen.labyrinthe_aleatoire(ligne,colonne)

### Étape 3 - Convertir le labyrinthe surdimensionné (tableau de booléens) en labyrinthe interprétable (tableau de Salles)
doors = mazeGen.passages(laby[0])

for i in range(ligneFin) :
    for j in range(colFin) :
        maze[i][j].setPorteN(doors[i][j]["nord"])
        maze[i][j].setPorteE(doors[i][j]["est"])
        maze[i][j].setPorteS(doors[i][j]["sud"])
        maze[i][j].setPorteO(doors[i][j]["ouest"])

for i in range(ligneFin) :
    for j in range(colFin) :
        print(str(maze[i][j].getPorteN()))