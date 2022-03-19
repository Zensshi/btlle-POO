import random
from random import randrange
import time

class Carte:
    """Représente une carte."""

    def __init__(self, symbole, valeur,):
        self.symbole = symbole
        self.valeur = valeur

    noms_symboles = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
    noms_valeurs = [None, 'AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']

    def __str__(self):
        return '%s de %s' % (Carte.noms_valeurs[self.valeur],
                             Carte.noms_symboles[self.symbole])

class Paquet:
    """Représente un paquet."""
    def __init__(self):
        self.cartes = []
        for symbole in range(4):
            for valeur in range(1, 14):
                carte = Carte(symbole, valeur)
                self.cartes.append(carte)

    def __str__(self):
        res = []
        for carte in self.cartes:
            res.append(str(carte))
        return '\n'.join(res)

    def pop_carte(self):
        return self.cartes.pop()

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def melanger(self):
        random.shuffle(self.cartes)

    def deplacer_cartes(self, main, nombre):
        for i in range(nombre):
            main.ajouter_carte(self.pop_carte())

p1 = Paquet()
print(p1)
print("==============================")

#Creation de la classe
class Main(Paquet):
    def __init__(self):
        self.cartes = self.__class__.__bases__[0]().cartes
        self.mainA = []
        self.mainB = []

 #Permet de tirer la premiere carte d'une des piles
    def tirer(self, pile):
        t = len(pile)
        if t >0:
            carte = pile[0]
            del(pile[0])
            return carte

#Permet de creer les deux jeux
    def creer_2jeux(self):
        self.melanger()
        for i in range(52):
            if i%2 == 0:
                self.mainA.append(self.cartes[i])
            else:
                self.mainB.append(self.cartes[i])

#Permet de comparer les deux jeux et les remets au gagnants
    def match(self, anciengain):
        carteA = self.tirer(self.mainA)
        carteB = self.tirer(self.mainB)
        if anciengain:
            if carteA == None:
                carteA = anciengain[-2]
                anciengain.remove(anciengain[-2])
            if carteB == None:
                carteB = anciengain[-1]
                anciengain.remove(anciengain[-1])
            gain = anciengain
        else:
            gain = []
        gain.append(carteA)
        gain.append(carteB)

        print(carteA)
        print("vs")
        print(carteB)
        print('\033[31m'+ "==============================" + '\033[0m')
        print("Vous êtes au "+str(tour)+"e tour.")

        if carteA.valeur > carteB.valeur:
            self.mainA.extend(gain)
            print ("Vous gagnez!")
            print (" ")

        elif carteB.valeur > carteA.valeur:
           self.mainB.extend(gain)
           print ("L'ordinateur gagne!")
           print(" ")

        elif carteB.valeur == carteA.valeur:
            print("Bataille !")
            gA=self.tirer(self.mainA)
            if gA == None:
                gA = carteA
            gB=self.tirer(self.mainB)
            if gB == None:
                gB = carteB
            gain.append(gA)
            gain.append(gB)

            return(self.match(gain))

        print ("Il vous reste %s carte(s)" % (len(self.mainA)))
        print ("Il reste %s carte(s) a l'ordinateur" % (len(self.mainB)))
        print (" ")
        print ('\033[32m'+ "NOUVEAU TOUR" + '\033[0m')

    def verif(self):
        if len(self.mainA) == 0 or len(self.mainB) == 0:
            return False
        else:
            return True


#Programme
if __name__ == '__main__':
    jeux = Main()
    print ("distribution des cartes...")
    time.sleep(2)
    jeux.creer_2jeux()
    print ("les jeux sont crées!")
    print ("==============================")
    tour=0

    while jeux.verif():
        if tour >= 2000:
            break
        a=input('Appuyez sur Entrée pour tirer une carte ou écrivez "skip" pour avoir le resultat : ')
        print('\033[31m'+ "==============================" + '\033[0m')
        if a == "skip":
            while jeux.verif() and tour < 1000000:
                jeux.match(None)
                tour+=1
        else:
            jeux.match(None)
            tour+=1


    if len(jeux.mainA) == 0:
        print ('\033[35m'+ "Vous avez perdu..." + '\033[0m')

    elif len(jeux.mainB) == 0:
        print ('\033[33m'+ "Vous avez gagné !!!!!!" + '\033[0m')

    else:
        print("Egalite")