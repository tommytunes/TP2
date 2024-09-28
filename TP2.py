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

for row in c: # for cle, item in d.items():
    if row[3] == 'cote_rangement':
        continue
    bibliotheque[row[3]] = {'titre' : row[0], 'auteur' : row[1] , 'date_publication' : row[2]}
    print(f' \n Bibliotheque initial : {bibliotheque[row[3]]} \n')



csv_collecbiblio.close()

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

nouvelle_collection = open('nouvelle_collection.csv', newline ='')

d = csv.reader(nouvelle_collection)

for row_2 in d:
    
    titre = row_2[0]
    auteur = row_2[1]
    date_publication = row_2[2]
    new_cote = row_2[3]

    if new_cote in bibliotheque:
       print(f"Le livre {new_cote} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque")
      
    else:
       bibliotheque[new_cote] = {'titre' : titre, 'auteur' : auteur, 'date_publication' : date_publication}
       print(f"Le livre {new_cote} ---- {titre} par {auteur} ---- a été ajouté avec succès")




########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

for row_3 in range(22, 45):
    bibliotheque['WS0'+ str(row_3)] = bibliotheque.pop('S0'+str(row_3))
    print("\n Bibliotheque avec modifications de cote :" "WS0" + str(row_3))





########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






