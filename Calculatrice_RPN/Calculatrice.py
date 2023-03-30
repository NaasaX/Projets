
#Imporation des bibliothèques

from math import*

op1=("+","-","*","**","/")  #premier tuple pour les opérateurs qui ont besoins de deux valeurs
op2=("sin","cos","tan","exp","log","log10") #deuxieme tuple pour les opérateurs qui ont besoins d'une seule valeur 


class calculatrice:

#Constructeur

    def __init__(self, limite=8):
        self.pile = []
        self.limite = limite
        self.valeur=[]

    #Ajoute une valeur à la pile
    def empiler(self, valeur):
            if self.taille() == self.limite:
                self.pile.pop(0)
            else:
                self.pile.append(valeur)

    #Enleve une valeur à la pile et la retourne
    def depiler(self):
        if len(self.pile) > 0:
            return self.pile.pop()
        else:
            return None

    #Retourne la hauteur de la pile 
    def taille(self):
        return len(self.pile)

    #Renvoie un booléen en fonction si le pile est vide ou non
    def pileestvide(self):
        if len(self.pile) == 0:
                return True
        else:
            return False

    #Affiche le résultat de la pile
    def voir(self):
        print()
        if self.pileestvide():  
            print("| vide |\n")
        else:
            copie = calculatrice()  
            while not self.pileestvide():
                element = self.depiler()  
                print("| "+str(element),"|")	
                copie.empiler(element) 
            print()
            while not copie.pileestvide():
                self.empiler(copie.depiler())
    

# ░█████╗░░█████╗░██████╗░███████╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░
# ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░
# ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░
# ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░
# ╚█████╔╝╚█████╔╝██████╔╝███████╗  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗
# ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝

pile= calculatrice()

choix=""

#Menu de choix

while choix!="q":   #Boucle tant que q n'est pas rentrer 
    choix=input("Entrer votre valeur : ")   #input pour ajouter les valeurs
    try:
        if choix!="q":
            if choix=="s":
                pile.depiler()
            elif choix=="pi":   #Ajout de la valeur pi 
                pile.empiler(pi)
            elif choix in op1:  #Calcul avec les opérateurs du premier tuple
                    valeur1=pile.depiler()
                    valeur2=pile.depiler()
                    pile.empiler(eval(str(valeur2)+choix+str(valeur1)))
            elif choix in op2:  #Calcul avec les poérateurs du deuxieme tuple
                    valeur1=pile.depiler()
                    pile.empiler(eval(choix+"("+str(valeur1)+")"))
            else:
                pile.empiler(float(choix))  #Ajout des valeurs
            pile.voir()
    except:
        print("Error")
            


