#################################################################################################################################
###                                                Interprète - Version 2.1                                                   ###
#################################################################################################################################
### "On avait les pièces détachées, on commence à assembler le véhicule" -Loïc DORNEL                                         ###
###===========================================================================================================================###

#################################################################################################################################

# Importation des différents modules et programmes complémentaires
import classes as cls
import commande as cmd
import sousFonctions as subFc
import labyrinthe_aleatoire as mazeGen
import genMaze

###---------------------------------------------------------------------------------------------------------------------------###
import tkinter as tk

#################################################################################################################################
# Déclaration des Items
bouclier = cls.Item("Bouclier", False, True, 1, True, True, subFc.recupDesc("item-bouclier"))
grosseCle = cls.Item("Grosse clé", False, True, 1, False, True, subFc.recupDesc("item-grosseCle"))

#################################################################################################################################
# Déclaration des Mecanisms
armure = cls.Mecanism("Armure", bouclier, grosseCle, True, subFc.recupDesc("meca-armure"), subFc.recupDesc("meca-armure-res"))

#################################################################################################################################
# Déclaration des Transports

#################################################################################################################################
# Récupération des fichiers textes
introFichier = open("Backstory.txt",'r', encoding="utf-8")
intro = introFichier.read()
introFichier.close()

#################################################################################################################################
# Lignes de texte variables
titre = "LE DONJON D'AZORIUS"
instruction = "Saisissez COMMENCER et appuyez sur ENTRÉE pour commencer"
madeBy = "Jeu réalisé par Loïc DORNEL et Anne PEREZ - L2 USMB 2019"

#################################################################################################################################
# Constantes de paramètres Tkinter
colBack = "#d2aa77"
Beng15 = ("Benguiat Bk BT", 15)
Beng20 = ("Benguiat Bk BT", 20)
Beng44 = ("Benguiat Bk BT", 44)

#################################################################################################################################
# Variables globales
newGame = True
currentX = ((genMaze.laby[1][0] - 1) // 2)
currentY = ((genMaze.laby[2][0] - 1) // 2)
salleCurrent = genMaze.maze[currentX][currentY]

#################################################################################################################################
# Sous-fonctions Tkinter
def clavier(event):
    global newGame
    global currentX
    global currentY
    touche = event.keysym
    if touche == "Return" :
        commande = entree.get()
        # Cas particulier 1 : Lancement du jeu
        if commande == "COMMENCER" and newGame :
            desc.config(text=salleCurrent.desc)
            titre.config(text="")
            newGame = False
        # Cas particulier 2 : ALLER
        if commande.split()[0].lower() == "aller" and not(newGame) :
            res = cmd.aller(commande.split()[1],currentX,currentY)
            currentX = res[0]
            currentY = res[1]

        ### MODE DEBUG
        if commande == "DEBUG pos" :
            print("X :",currentX)
            print("\n")
            print("Y :",currentY)
        # Dans tous les cas, on efface le contenu en appuyant sur ENTER
        entree.delete(0,tk.END)

#################################################################################################################################
# Fenêtre Tkinter
fen = tk.Tk()

fen.configure(background=colBack)

fen.rowconfigure(0,weight=1)
fen.columnconfigure(0,weight=1)

desc = tk.Label(fen,text=intro,bg=colBack,font=Beng15,justify=tk.LEFT,wraplength=1920)
desc.grid(row=0,sticky='nw')

titre = tk.Label(fen,text=titre,bg=colBack,font=Beng44)
titre.grid(row=1)

soustitre = tk.Label(fen,text=instruction,bg=colBack,font=Beng20)
soustitre.grid(row=2)

credit = tk.Label(fen,text=madeBy,bg=colBack,font=Beng15)
credit.grid(row=3)

entree = tk.Entry(fen,bg=colBack,font=Beng15)
entree.grid(sticky='sew')

fen.focus_set()
fen.bind("<Key>", clavier)
fen.grid()
#################################################################################################################################
###\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/###
###/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\###
#################################################################################################################################
fen.mainloop()