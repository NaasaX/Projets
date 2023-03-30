    #|Importation des bibliothèques|

from cProfile import label
from math import *
from tkinter import *

    #|Variables|

def clic_calcul():      #def qui permet de calculer lors du clic
    resultat.configure(text="Votre résultat est : "+str(eval(saisie.get())))

def calcul(event):      #def qui permet de calculer lors de l'appuie du bouton entré 
    resultat.configure(text="Votre résultat est : "+str(eval(saisie.get())))

def effacer_calcul():      #def qui permet de supprimer le contenu de la case saisie et supprime la case de résultat
    saisie.delete(0,END)
    resultat.configure(text="")

    #|Code Principal|

calculatrice=Tk()
calculatrice.title("Calculatrice")      #Nom de la fenêtre 
calculatrice.maxsize(width=400,height=250)      #Taille max de la fenêtre 
calculatrice.minsize(width=400,height=250)      #Taille min de la fenêtre
calculatrice.configure(bg="black")      #Couleur du fond
calculatrice.bind("<Return>",calcul)    #Bind de la touche Entrer 


texte=Label(calculatrice,text="Entre ton calcul",bg="grey")   #Texte Label
texte.pack()
saisie=Entry(calculatrice,width=30,bg="grey")     #Case de saisie 
saisie.pack()
entrer=Button(calculatrice,width=20,text="Valider",bg="green1",command=clic_calcul)     #Bouton 
entrer.pack()
resultat=Label(calculatrice,bg="grey")    #Case de résultat
resultat.pack()
effacer=Button(calculatrice,width=20,text="Effacer",command=effacer_calcul,bg="grey")     #Bouton Effacer la case saisie
effacer.pack()
bouton_quitter=Button(calculatrice, text="Quitter",bg="red", command=calculatrice.quit)     #Bouton Quitter
bouton_quitter.pack()

calculatrice.mainloop()     #Ouvre la fenêtre 
