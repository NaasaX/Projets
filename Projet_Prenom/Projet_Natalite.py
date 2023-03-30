#Importation des bibliothèques

from csv import*

# Ouverture du fichier

def ouverture_fichier():

    fichier = open('nat2020.csv', 'r', encoding="UTF8")
    lecteur = reader(fichier, delimiter=';')
    donnees = []
    for ligne in lecteur:
        donnees.append(ligne)

    fichier.close()

    return donnees

# Fonctions

# Requete 1

def requete1(donnees, prenom, annee):
    for ligne in donnees:
        if ligne[1] == prenom and ligne[2] == annee:
            return int(ligne[3])
    return None

# Requete 2


def requete2(donnees, annee):

    effectif_rares = 0
    effectif_garcon = 0
    prenom_garcon = ""
    prenom_rares = ""

    for ligne in donnees:
        if ligne[2] == annee:
            if ligne[0] == "1":
                if ligne[1] != "_PRENOMS_RARES":
                    if int(ligne[3]) > effectif_garcon:
                        effectif_garcon = int(ligne[3])
                        prenom_garcon = ligne[1]


    effectif_fille = 0
    prenom_fille = ""

    for ligne in donnees:
        if ligne[2] == annee:
            if ligne[0] == "2":
                if ligne[1] != "_PRENOMS_RARES":
                    if int(ligne[3]) > effectif_fille:
                        effectif_fille = int(ligne[3])
                        prenom_fille = ligne[1]
                    

    return (effectif_garcon, prenom_garcon, effectif_fille, prenom_fille)


# Requete 3

def requete3(donnees, prenom):
    maxi = 0
    annee = ""
    for ligne in donnees:
        if ligne[3] != "XXXX":
            if ligne[1] == prenom:     
                if int(ligne[3]) > maxi:
                    maxi = int(ligne[3])
                    annee = ligne[2]
    if annee == "":
        return None
    else:
        return (annee, maxi)


# Menu Principal

donnees = ouverture_fichier()
choix = " "

# Menu des choix 

while choix != "q":
	print("Tous les choix possibles :\n")
	print("La requete1 permet de savoir le nombre de de prénoms donnés pour une année.")
	print("La requete2 permet de d'afficher le nombre de prénoms donnés au maximum pour une année.")
	print("La requete3 permet de choisir un prénom pour avoir l'année où il y a l'effectif maximal.\n")
	choix = input("Entrer votre choix : ")

# Choix requete1

	if choix == "requete1":
		prenom = input("Entrer un prénom : ").upper()       #upper pour mettre en majuscule le prénom entré
		annee = input("Entrer une année : ")
		reponse = requete1(donnees, prenom, annee)
		print("En ", annee, ", il y a",prenom,reponse, "qui sont né(e)(s).\n")      #Afficher la réponse
		
# Choix requete2

	if choix == "requete2":
		annee = input("Entrer une année : ")
		reponse = requete2(donnees, annee)
		prenom_garcon = reponse[1]
		prenom_fille = reponse[3]
		effectif_garcon = reponse[0]
		effectif_fille = reponse[2]
		print("En ", annee, ", le prénom le plus courant est ",prenom_garcon,"il y a eu",effectif_garcon,"naissances.\n")       #Afficher la réponse
		print("En ", annee, ", le prénom le plus courant est ",prenom_fille,"il y a eu",effectif_fille,"naissances.\n")     #Afficher la réponse

# Choix requete3

	if choix=="requete3":
		prenom=input("Entrer un prénom :").upper()      #upper pour mettre en majuscule le prénom entré
		reponse=requete3(donnees,prenom)
		maxi = reponse[1]
		annee = reponse[0]
		print("Le prénom",prenom,"a été donné(e) au maximum",maxi,"fois en",annee,".\n")       #Afficher la réponse
