
#Fonction

def ConvBinDec (nbinaire):  #Fonction pour convertir un nombre binaire en décimal
    ndecimal=0
    nbits=len(nbinaire)
    for i in range(nbits):
        ndecimal=ndecimal+int(nbinaire[nbits-1-i])*2**i 
    return ndecimal

def ConvDecBin(n):  #Fonction pour convertir un nombre décimal à un nombre binaire
    reste=0
    quotient=1
    quotient=n
    resultat=" "
    while quotient!=0 : 
        reste=quotient%2
        quotient=quotient//2
        resultat=str(reste)+resultat
    return resultat 

def ConvDecBase(n,b):   #Fonction pour convertir un nombre
    reste=0
    quotient=1
    quotient=n
    resultat=" "
    while quotient!=0 : 
        reste=quotient%b
        quotient=quotient//b
        resultat=str(reste)+resultat
    return resultat 

def ConvBaseDec(nbase,b):   #Fonction pour convertir un nombre de base b à un nombre décimal
    ndecimal=0
    nbits=len(nbase)
    for i in range(nbits):
        ndecimal=ndecimal+int(nbase[nbits-1-i])*b**i 
    return ndecimal

def NombreValide(nombre,b): #Fonction bouléenne 
    nombredechiffre=len(nombre)
    for i in range(nombredechiffre):
        chiffre=int(nombre[i])
        if chiffre>=b: 
            return False
    return True

def ConvBaseBase(nbase,b1,b2):  #Fonction Pour convertir un nombre de base b en base b
    ndecimal=ConvBaseDec(nbase,b1)
    return ConvDecBase(ndecimal,b2)


#Code Principal 

print("Convertisseur multibase")
print("*****************************")
choix=" "


#Menu de Choix
while choix!="q":
    print("\nTaper 1 pour convertir un nombre binaire à un nombre décimal")
    print("\nTaper 2 pour convertir un nombre décimal à un nombre binaire") 
    print("\nTaper 3 pour convertir un nombre décimal à un nombre de la base b")
    print("\nTaper 4 pour convertir de la base b à un nombre décimal")
    print("\nTaper Q pour quitter")
    choix=input("\nVotre choix : ")
    print ()
#Choix 1
    if choix=="1":
        nbinaire=(input("Donner le nombre binaire : ")) #Nombre décimal à nombre binaire
        print("Le nombre binaire" ,nbinaire, "est égal à" ,ConvBinDec(nbinaire), "en décimal")
#Choix 2
    if choix=="2":
        n=int(input("Donner le nombre décimal à convertir : ")) #Nombre binaire à nombre décimal
        print(ConvDecBin(n))
#Choix 3
    if choix=="3":
        b=int(input("Choisir la base dans laquelle convertir : "))
        n=int(input("Donner le nombre décimal à convertir : ")) #Nombre décimal à nombre de la base b
        
        print(ConvDecBase(n,b))
#Choix 4 
    if choix=="4":
        b=int(input("Choisir la base dans laquelle convertir : "))
        nbase=(input("Donner le nombre en base b : ")) #Nombre de la base b à nombre décimal
        
        print(ConvBaseDec(nbase,b)) 