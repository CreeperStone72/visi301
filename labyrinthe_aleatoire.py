import random
import pygame
def matrice_initiale(ligne,colonne):

    #Génération d'une matrice de dimension ligne*colonne
    #remplie de False

    matrice=[]
    for i in range (0,ligne):
        matrice.append([False]*colonne)
    return matrice

def case_initiale(matrice):
    #Choix de la case de départ du labyrinthe symbolisé par matrice avec une ligne
    #sur 2 et une colonne sur 2 qui correspondent à des murs
    #La bordure du labyrinthe est aussi faite de murs

    #Prend en entrée une matrice avec pour valeurs des booléens
    #retourne les coordonnées de la case libre choisie au hasard

    #On prend les dimensions de la matrice
    ligne=len(matrice)
    colonne=len(matrice[1])

    #On initialise les listes des lignes et des colonnes de cases libres
    liste_ligne=[]
    liste_colonne=[]

    #Parcours des lignes qui ne sont pas des murs
    for i in range(1, ligne-1, 2):

        #Liste des lignes qui ne sont pas des murs
        liste_ligne.append(i)

    #Choix au hasard d'une ligne
    choix_indice_ligne=random.randint(0,len(liste_ligne)-1)
    choix_ligne=liste_ligne[choix_indice_ligne]

    #Parcours des colonnes qui ne sont pas des murs
    for i in range(1, colonne-1, 2):
        liste_colonne.append(i)
    #Choix au hasard d'une colonne qui n'est pas un mur
    choix_indice_colonne=random.randint(0,len(liste_colonne)-1)
    choix_colonne=liste_colonne[choix_indice_colonne]


    return [choix_ligne,choix_colonne]

def voisine(case,matrice):

    #Fonction qui prend en entrée une liste "case" avec pour 1er élément la ligne de
    #la case dont on veut connaitre les voisines et pour 2nd élément sa colonne
    #Fonction qui prend aussi en entrée la matrice contenant l'ensemble des cases

    #Fonction qui retourne une liste "lignes_voisines" des lignes
    #des cases voisines d'une case hors celles en diagonale
    #Et une liste colonne_voisines des abscisse colonnes de ces cases voisines

    #Dimensions de la matrice
    ligne=len(matrice)
    colonne=len(matrice[1])

    #Initialisation de la liste des lignes et la liste des colonnes des cases voisines
    ligne_voisines=[]
    colonne_voisines=[]
    for i in (-2,2):
        #Parcours des cases voisines sur la même colonne

        #Si la case voisine parcourue ne sort pas des limites du labyrinthe
        if case[0]+i!=-1 and case[0]+i!=ligne:
            ligne_voisines.append(case[0]+i)
            #Dans la liste des colonnes, on mettra le numéro de la colonne parcourue
            colonne_voisines.append(case[1])


    for j in (-2,2):
        #Parcours des cases voisines sur la même ligne

        #Si la case voisine ne sort pas des limites de la matrice
        if case[1]+j!=-1 and case[1]+j!=colonne:
            colonne_voisines.append(case[1]+j)
            ligne_voisines.append(case[0])


    return [ligne_voisines,colonne_voisines]

def voisines_non_visitees(cases_voisines,matrice):

    #Fonction qui prend en entrée la liste des abscisses et la liste des ordonnées
    #des cases voisines d'une case ainsi que la matrice contenant toutes les cases
    #Et retourne la liste des abscisses et la liste des ordonnées des cases voisines
    #non visitées (donc avec un false)

    #Dimensions de la matrice
    ligne=len(matrice)
    colonne=len(matrice[1])

    #Initialisation du compteur du nombre de cases voisines visitées
    nombre_visite=0
    #Initialisation de la liste des lignes de voisines non visitées
    ligne_non_visitee=[]
    #Initialisation de la liste des colonnes de voisines non visitées
    colonne_non_visitee=[]

    #Parcours des cases voisines
    for i in range (0,len(cases_voisines[0])):

        #Si la case voisine n'a pas été visitée donc la matrice contient un false
        if matrice[cases_voisines[0][i]][cases_voisines[1][i]]==False:

            #On ajoute l'abscisse et l'ordonnée de la case considérée aux listes
            #des lignes et colonnes de cases non visitées
            ligne_non_visitee.append(cases_voisines[0][i])
            colonne_non_visitee.append(cases_voisines[1][i])

            #On compte cette case non visitée
            nombre_visite=nombre_visite+1

    return [ligne_non_visitee, colonne_non_visitee, nombre_visite]


def voisine_aleatoire(non_visitee,matrice):

    #Fonction qui prend en entrée la liste des lignes des cases voisines non visiées
    #et celle des ordonnées ainsi que le nombre de voisines visitées sous forme d'une tableau
    #Et prend en entrée la matrice des cases

    #Retourne une liste de deux éléments: une ligne et une colonne de la voisine
    #non visitée sélectionnée au hasard.

    #Sélection au hasard de l'indice dans la liste des abscisses et des ordonnées
    indice=random.randint(0,len(non_visitee[0])-1)

    #retour des abscisses et ordonnées correspondant à cet indice
    return [non_visitee[0][indice],non_visitee[1][indice]]

def marquer_visite(coordonnees_voisine,matrice):
    #prend en entrée la case voisine non visitee de la matrice ainsi que la matrice
    #Marque cette case comme visitée en lui assignant la valeur True
    #Retourne la matrice avec ce booléen modifié

    matrice[coordonnees_voisine[0]][coordonnees_voisine[1]]=True

    return matrice



def tomber_mur(case,coordonnees_voisine,matrice):
    #Fonction qui "détruit" le mur (symbolisé par un false) entre la case considérée
    #et sa voisine libre choisie au hasard.
    #Prend en entrée la matrice considérée et la case et sa voisine
    #Retourne la matrice avec true à l'emplacement du mur tombé

    #Initialisation d'une liste avec pour 1er élément la ligne du mur et pour 2nd élément sa colonne
    mur=[]

    #Si la case et sa voisine sont sur la même ligne
    if case[0]==coordonnees_voisine[0]:
        #On met les coordonnées du mur dans la liste mur
        mur.append(case[0])
        mur.append(int((case[1]+coordonnees_voisine[1])/2))

    #Si la case et sa voisine sont sur la même colonne
    if case[1]==coordonnees_voisine[1]:
        mur.append(int((case[0]+coordonnees_voisine[0])/2))
        mur.append(case[1])

    #On modifie la valeur de la case de la matrice aux coordonnées "mur" en True
    matrice[mur[0]][mur[1]]=True

    return matrice

def verification(matrice):

    #Prend en entrée la matrice dont on veut vérifier si toutes les cases
    #libres ont déjà été visitées.

    #Retourne la variable que_des_true qui retourne true si toutes les cases
    #ont été visitées, false sinon

    #On prend les dimensions de la matrice
    ligne=len(matrice)
    colonne=len(matrice[1])

    #Initialisation de que_des_true
    Que_des_true=True
    #Parcours des cases libres (pas des murs) de la matrice
    for i in range (1,ligne-1,2):
        for j in range(1,colonne-1,2):
            #Dès qu'on tombe sur un false (case non visitée)
            if matrice[i][j]==False:
                Que_des_true=False
    return Que_des_true

def labyrinthe_aleatoire(line,column):

    #Initialisation de la matrice avec uniquement des false
    matrice=matrice_initiale(line,column)

    #Initialisation de listes qui contiendront les lignes et colonnes des cases visitées
    ligne_chemin=[]
    colonne_chemin=[]

    #On choisit aléatoirement la première case du labyrinthe et on la marque comme visitée
    case=case_initiale(matrice)
    matrice[case[0]][case[1]]=True

    #On ajoute ses coordonnées au chemin
    ligne_chemin.append(case[0])
    colonne_chemin.append(case[1])
    #On est dans la première case du chemin donc à l'indice 0
    indice_chemin=0

    #On rentre dans la boucle en vérifiant que toutes les cases n'ont pas été visitées
    Que_des_true=verification(matrice)

    #S'il reste des cases non visitées
    while Que_des_true==False:

        #On prend les coordonnées des cases voisines de la case courante
        cases_voisines=voisine(case,matrice)
        #On ne garde que celles qui n'ont pas été visitées s'il y en a
        non_visitee=voisines_non_visitees(cases_voisines,matrice)

        #Tant que la case consideree n'a pas de voisines non visitées et qu'on
        #n'est pas revenu à a case initiale
        while non_visitee[2]==0 and indice_chemin!=0:

            #On revient en arrière dans le chemin
            indice_chemin=indice_chemin-1

            #On prend les coordonnées de la case précédente dans le chemin
            case=[]
            case.append(ligne_chemin[indice_chemin])
            case.append(colonne_chemin[indice_chemin])
            #On les remet dans la liste du chemin
            ligne_chemin.append(case[0])
            colonne_chemin.append(case[1])
            #On prend les coordonnées de ses voisines
            cases_voisines=voisine(case,matrice)
            #Parmi ses voisines, on regarde celles qui n'ont pas été visitées
            non_visitee=voisines_non_visitees(cases_voisines,matrice)

        #S'il y a au moins une case voisine non visitée
        if non_visitee[2]!=0:

            #On choisit aléatoirement une voisine non visitée et on prend ses coordonnées
            coordonnees_voisine=voisine_aleatoire(non_visitee,matrice)
            #On marque la cases choisie comme visitee avec un true
            matrice=marquer_visite(coordonnees_voisine,matrice)
            indice_chemin=indice_chemin+1
            #On met ses coordonnées dans la liste des lignes et colonnes visitées
            ligne_chemin.append(coordonnees_voisine[0])
            colonne_chemin.append(coordonnees_voisine[1])
            #On supprime le mur entre la case choisie et la case initialement considérée
            matrice=tomber_mur(case,coordonnees_voisine,matrice)
            #On prend comme case courante la nouvelle case choisie
            case=[]
            case.append(coordonnees_voisine[0])
            case.append(coordonnees_voisine[1])


        #On vérifie si toutes les cases ont été visitées
        Que_des_true=verification(matrice)

    return [matrice,ligne_chemin,colonne_chemin]


def portes(ligne,colonne,matrice):
#Prend en entrée la matrice avec des booléens représentant le labyrinthe
#aléatoire et les coordonnées d'une de ses pièces

#Retourne pour cette pièce les portes accessibles indiquées par true
#et les portes inaccessibles par false
    liste_portes={}
    #1er élément de la liste: porte nord, 2) porte est 3) porte sud
    #4) porte ouest
    liste_portes["nord"]=matrice[ligne-1][colonne]
    liste_portes["est"]=matrice[ligne][colonne+1]
    liste_portes["sud"]=matrice[ligne+1][colonne]
    liste_portes["ouest"]=matrice[ligne][colonne-1]

    return liste_portes

def passages(matrice):
    #Prend en entrée la matrice retournée par labyrinthe_aleatoire
    #Retourne matrice_portes dont chaque case correspondra à un dictionnaire
    #de portes ayant pour valeur true ou false selon qu'il y a un passage ou non
    matrice_portes=[]
    ligne=len(matrice)
    colonne=len(matrice[0])
    #On initialise toutes les portes à False
    liste_init={}
    liste_init["nord"]=False
    liste_init["est"]=False
    liste_init["sud"]=False
    liste_init["ouest"]=False
    for i in range (0,int((ligne-1)/2)):
        matrice_portes.append([liste_init]*int((colonne-1)/2))
    #On parcourt la matrice entrée
    for i in range (1,ligne-1,2):
        for j in range(1,colonne-1,2):
            #On cherche la valeur de ses portes qu'on met dans
            #matrice_portes qui ne prend en compte que des cases effectives (et non
            #les murs et bords)
            liste_portes=portes(i,j,matrice)
            matrice_portes[int((i-1)/2)][int((j-1)/2)]=liste_portes
    return matrice_portes





def mecanisme(matrice_chemin,nb_meca):

#Prend en entrée le labyrinthe et le chemin ainsi que le nombre de mécansimes à placer

#Longueur du chemin
    fin=len(matrice_chemin[1])
#Liste qui donnera les positions des cses dans le chemin choisies au hasard pour abriter des mécanismes
    choix=[]

    #1er choix: on laisse nb_meca+1 cases libres après ce choix dans le chemin pour pouvoir être sûr
    #d'avoir la place de caser les mécanismes suivants
    choix.append(random.randint(0,fin-nb_meca))

    #POur les autres choix on choisira parmi les cases du chemin situées après la case choisie pour le
    #mécanisme précédent
    for i in range(1,nb_meca):
        #Choix de la case du mecanisme
        #On part de la cases choisie précédemment et on choisit parmi les cases restantes après dans
        #le chemin
        choix.append(random.randint(choix[i-1]+1,fin-nb_meca+i))

    return choix


def affichage(line,column,nb_meca):

    #Affiche le labyrinthe avec la case de départ et celle d'arrivée
    #ainsi que le numero des mécansimes placés au hasard dans l'ordre

    #Construction du labyrinthe
    matrice_chemin=labyrinthe_aleatoire(line,column)

    matrice=matrice_chemin[0]

    #Longueur du chemin
    fin=len(matrice_chemin[1])
    #Largeur des cases (carrées)
    pas=50

#Choix au hasard des positions des mécanismes
    choix=mecanisme(matrice_chemin,nb_meca)


#Initialisation des couleurs
    white=(255,255,255)
    black=(0,0,0)
    blue = (0, 0, 180)
    red = (255, 0,0)
    green = (0, 255, 0)

#Affichage d'un ecran blanc
    pygame.init()
    ecran=pygame.display.set_mode((line*pas, column*pas))
    ecran.fill(white)
    pygame.display.update()


#La fenêtre reste affichée et se ferme quand on appuis sur une touche
    continuer=True
    while continuer:
        for i in range(0, line):
            for j in range(0,column):
                #On remplit de noir les cases avec False pour faire les murs
                if matrice[i][j]==False:
                    pygame.draw.rect(ecran, black, (i*pas, j*pas, pas, pas))

        #On remplit de bleu la case de départ
        pygame.draw.rect(ecran,blue,(matrice_chemin[1][0]*pas, matrice_chemin[2][0]*pas, pas, pas))
        #On remplit de rouge la case d'arrivée
        pygame.draw.rect(ecran,red,(matrice_chemin[1][fin-1]*pas, matrice_chemin[2][fin-1]*pas, pas, pas))


        #On marque le numero du mécanisme dans la case
        for i in range(0,nb_meca):
            font_obj = pygame.font.Font('freesansbold.ttf', 32)
            text_surface_obj = font_obj.render(str(i), True, green, blue)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (matrice_chemin[1][choix[i]]*pas+pas/2, matrice_chemin[2][choix[i]]*pas+pas/2)
            ecran.blit(text_surface_obj, text_rect_obj)
        #On affiche le labyrinthe
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:#Pour fermer la fenêtre en appuyant sur une touche
                continuer=False

    pygame.quit()