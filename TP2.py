"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

bibliotheque = {}
csv_collecbiblio = open('collection_bibliotheque.csv', newline ='')

c = csv.reader(csv_collecbiblio)

for row in c:
    if row[3] == 'cote_rangement':
        continue
    bibliotheque = {row[3] : {row[0] : 'titre', row[1] : 'auteur', row[2] : 'date_publication'}}
    print(bibliotheque)

print(f' \n Bibliotheque initial : {c} \n')

csv_collecbiblio.close()

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici






########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






