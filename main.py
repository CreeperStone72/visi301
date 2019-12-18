#################################################################################################################################
###                                                Interprète - Version 2.1                                                   ###
#################################################################################################################################
### "On avait les pièces détachées, on commence à assembler le véhicule" -Loïc DORNEL                                         ###
#################################################################################################################################

# Importation des différents modules et programmes complémentaires
import classes as cls
import commande as cmd
import sousFonctions as subFc
import genMaze

###---------------------------------------------------------------------------------------------------------------------------###
import tkinter as tk
import tkinter.messagebox as msg

#################################################################################################################################
# Récupération des fichiers textes
introFichier = open("Backstory.txt", 'r', encoding = "utf-8")
intro = introFichier.read()
introFichier.close()

outroFichier = open("Epilogue.txt", 'r', encoding = "utf-8")
outro = outroFichier.read()
outroFichier.close()

#################################################################################################################################
# Lignes de texte variables
title = "LE DONJON D'AZORIUS"
instruction = "Saisissez COMMENCER et appuyez sur ENTRÉE pour commencer"
madeBy = "Jeu réalisé par Loïc DORNEL et Anne PEREZ - L2 USMB 2019"
thanks = "Merci d'avoir joué !"
droitsAWB = "L'histoire et la géographie de la Terre de Flunes appartiennent à AperWorldBuilding."
droitsDdN = "Toutes les références au Donjon de Naheulbeuk appartiennent à John \"Pen of Chaos\" Lang."

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
    global salleCurrent
    touche = event.keysym
    erreur = ""

    # On continue de jouer tant que l'on n'est pas libre. Logique...
    if not(genMaze.freedom.exists) :
        if touche == "Return" :
            commande = entree.get()

            # Cas particulier 1 : Lancement du jeu
            if commande == "COMMENCER" and newGame :
                desc.config(text = salleCurrent.desc)
                titre.config(text = "")
                soustitre.config(text = subFc.affiche_portes(salleCurrent))
                objets.config(text = subFc.affiche_objets(salleCurrent))
                inventory.config(text = subFc.affiche_inventaire())
                newGame = False

            if not(newGame) :
                    inst = commande.lower().split()[0]

                    # Cas particulier 2 : ALLER
                    if inst == "aller" :
                        res, erreur = cmd.aller(commande.lower().split()[1], currentX, currentY)
                        currentX = res[0]
                        currentY = res[1]
                        if erreur == "" :
                            salleCurrent = genMaze.maze[currentX][currentY]
                            desc.config(text = salleCurrent.desc)
                            soustitre.config(text = subFc.affiche_portes(salleCurrent))
                            objets.config(text = subFc.affiche_objets(salleCurrent))
                        else :
                            msg.showerror("Direction invalide", erreur)

                    elif inst in ["prendre", "poser"] :
                        t = False
                        obj = ' '.join(commande.lower().split()[1:])
                        if inst == "prendre" :
                            t = True
                        cmd.prendre_poser(obj, currentX, currentY, t)
                        objets.config(text = subFc.affiche_objets(salleCurrent))
                        inventory.config(text = subFc.affiche_inventaire())

                    elif inst == "utiliser" :
                        obj = commande.lower().split()[1:]
                        res, erreur = cmd.utiliser(obj, currentX, currentY)
                        if not(erreur == "") :
                            msg.showerror("Utilisation incorrecte", erreur)
                        else :
                            msg.showinfo("Utilisation réussie", res)
                            objets.config(text = subFc.affiche_objets(salleCurrent))
                            inventory.config(text = subFc.affiche_inventaire())

                    elif inst == "observer" :
                        obj = " ".join(commande.lower().split()[1:])
                        res, erreur = cmd.observer(obj)
                        if not(erreur == "") :
                            msg.showerror("404 description not found", erreur)
                        else :
                            msg.showinfo("Description", res)

                    # Dans tous les cas, on efface le contenu en appuyant sur ENTER
                    entree.delete(0,tk.END)

    # Une fois que l'on est libre, c'est gagné !
    else :
        desc.config(text = outro)
        titre.config(text = title)
        soustitre.config(text = thanks)
        objets.config(text = droitsAWB)
        inventory.config(text = droitsDdN)

#################################################################################################################################
# Fenêtre Tkinter
fen = tk.Tk()

fen.configure(background = colBack)

fen.rowconfigure(0, weight = 1)
fen.columnconfigure(0, weight = 1)

desc = tk.Label(fen, text = intro, bg = colBack, font = Beng15, justify = tk.LEFT, wraplength = 1920)
desc.grid(row = 0, sticky = 'nw')

titre = tk.Label(fen, text = title, bg = colBack, font = Beng44)
titre.grid(row = 1)

soustitre = tk.Label(fen, text = instruction, bg = colBack, font = Beng20)
soustitre.grid(row = 2)

objets = tk.Label(fen, text = "", bg = colBack, font = Beng15)
objets.grid(row = 3)

inventory = tk.Label(fen, text = "", bg = colBack, font = Beng15)
inventory.grid(row = 4)

credit = tk.Label(fen, text = madeBy, bg = colBack, font = Beng15)
credit.grid(row = 5)

entree = tk.Entry(fen, bg = colBack, font = Beng15)
entree.grid(sticky = 'sew')

fen.focus_set()
fen.bind("<Key>", clavier)
fen.grid()
#################################################################################################################################
###\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/###
###/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\###
#################################################################################################################################
fen.mainloop()