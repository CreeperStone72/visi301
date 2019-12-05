class Item :
    def __init__(self, name, inInventory, usable, uses, exists, canBeObserved, desc = "") :
        """Objets pouvant être ramassés et utilisés
        name : Le nom, une chaîne de caractères
        inInventory : L'objet est-il dans l'inventaire ?, un booléen
        usable : L'objet est-il compatible avec UTILISER ?, un booléen
        uses : Nombre d'utilisations avant que l'objet ne se casse et disparaisse, un entier. Est indestructible S'il vaut -1
        exists : L'objet est-il visible ?, un booléen
        canBeObserved : L'objet est-il compatible avec OBSERVER ?, un booléen
        desc : Description de l'objet, une chaîne de caractères"""
        self.name = name
        self.inInventory = inInventory
        self.usable = usable
        self.uses = uses
        self.exists = exists
        self.canBeObserved = canBeObserved
        self.desc = desc

class Mecanism :
    def __init__(self, name, objInteract, objFin, exists, desc, descRes) :
        """Objets étant la cible de UTILISER
        name : Le nom, une chaîne de caractères
        objInteract : L'objet outil de UTILISER, un Item
        objFin : L'objet résultat de UTILISER, un Item ou un Transport
        exists : Le mécanisme est-il visible ?, un booléen
        desc : Description du mécanisme, une chaîne de caractères
        descRes : Description de l'action réalisée par le mécanisme, une chaîne de caractères"""
        self.name = name
        self.objInteract = objInteract
        self.objFin = objFin
        self.exists = exists
        self.desc = desc
        self.descRes = descRes

class Transport :
    def __init__ (self, salle, pointCard, exists) :
        """Point de passage entre deux salles, créant un passage à sens unique
        salle : La salle où se trouve le point, une Salle
        pointCard : La porte concernée, une chaîne de caractères
        exists : Le point de passage est-il visible ?, un booléen"""
        self.salle = salle
        self.pointCard = pointCard
        self.exists = exists
    def ouverture(self) :
        self.salle.set(pointCard, True)

class Salle :
    def __init__(self, porteN = False, porteE = False, porteS = False, porteO = False, objets = [], mecas = [], desc = "") :
        """Lieu où se trouve le joueur
        porteN, porteE, porteS, porteO : Y a-t-il une porte au nord / à l'est / au sud / à l'ouest ?, un booléen
        objets : Ensemble des objets présents par terre dans la salle, une liste d'Items
        mecas : Ensemble des mécanismes présents dans la salle, une liste de Mecanism
        desc : Description de la salle, une chaîne de caractères"""
        self.porteN = porteN
        self.porteE = porteE
        self.porteS = porteS
        self.porteO = porteO
        self.objets = objets
        self.mecas = mecas
        self.desc = desc
    def setPorteN(self, value) :
        self.porteN = value
    def setPorteE(self, value) :
        self.porteE = value
    def setPorteS(self, value) :
        self.porteS = value
    def setPorteO(self, value) :
        self.porteO = value
    ###############################
    def getPorteN(self) :
        return self.porteN