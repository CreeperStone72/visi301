# Le Donjon d'Azorius

Vous êtes Taerntym Jacquerand, traqueur demi-elfe, se retrouve piégé à l'intérieur du Donjon d'Azorius en voulant retrouver deux de ses collègues disparus. Parviendrez-vous à trouver la sortie ?

## Mise en place du jeu sur votre machine

### Pré-requis

Vous devez avoir un interprète Python 3 ainsi que les modules suivants :

- pygame
- tkinter
- random

### Installation

Vous devez d'abord télécharger les fichiers Python suivants :

- main
- classes
- commande
- sousFonctions
- labyrinthe_aleatoire
- genMaze

Vous devez également récupérer les fichiers texte Backstory et Epilogue, que vous placerez dans le même dossier que les fichiers Python.

Après cela, ajouter le sous-dossier descriptions et tous les fichiers texte présents dedans dans ce même dossier.

Enfin, il vous faut télécharger le fichier BENGUIAB.TTF et l'exécuter afin d'installer la police de caractères Benguiat Bk BT utilisée par le programme si vous ne l'avez pas déjà.

## Démarrage

Pour démarrer le jeu, ouvrez main.py et compilez le programme.

Une fois la fenêtre ouverte, entrez 'COMMENCER' dans la zone de saisie en respectant la casse.

Vous commencez immédiatement dans le labyrinthe. Pour connaître les fonctions, leur syntaxe et leur structure, tapez 'help' dans la zone de saisie.

## Versions

**Version finale :** 2.1
_Les anciennes versions peuvent être retrouvées dans le dossier old._

**Version 2.1 - La version qui fonctionne**
- 5 commandes fonctionnelles
- Génération aléatoire de labyrinthes 1x1 (même si l'intérêt...) à 9x9 (le compilateur a trop de mal sur des tailles plus grandes)
- Interface graphique
- Arc narratif "complet"
- Une seule trame de progression dans le jeu

**Version 1.2 - La Proof of Concept côté interprète**
- 5 commandes fonctionnelles
- "Labyrinthe" 2x2 fixe
- Interface via la console

**Version 1.1 - Gestion de l'inventaire**
- 4 commandes fonctionnelles
- Une seule salle
- Interface via la console

_Les "versions" ci-dessous sont des programmes de tests. Ils peuvent également être retrouvés dans old._

**Version 0.1 - Idée pour commencer l'assemblage (entre les versions 1.2 et 2.1**
- Tentative d'attacher ensemble la génération de labyrinthe et l'interprète
- Échec → Toutes les cases pointent vers le même objet Salle (YaY)

**Interface utilisateur - ou comment j'ai arrêté de débugger et ai commencé à vouloir un jeu beau**
- Interface graphique

**testCOMMANDE - Les quatre vrais premiers programmes de test**
- Une ou deux (pour PRENDRE-POSER) commandes fonctionnelles par sous-programme
- Interface via la console

**Interpréteur - Chemin original abandonné**
- Le premier fichier Python du projet
- La documentation de 100 lignes s'est révélée inutile après que l'on ait changé de direction complètement

## Auteurs

* **Anne Perez** _alias_ [@AnneIna](https://github.com/AnneIna) (_répertoire visi301-1 accessible [ici](https://github.com/AnneIna/visi301-1))_
* **Christopher Stone** _alias_ [@CreeperStone72](https://github.com/CreeperStone72)
