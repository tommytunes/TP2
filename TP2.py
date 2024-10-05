"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 05
Numéro d'équipe :  26
Noms et matricules :Thomas Staples (2371342), Mohamed Amine Mahboubi (2391873)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

import csv

bibliotheque = {}
csv_collecbiblio = open('collection_bibliotheque.csv', newline ='')

c = csv.reader(csv_collecbiblio)

for row in c: 
    if row[3] == 'cote_rangement':
        continue
    bibliotheque[row[3]] = {'titre' : row[0], 'auteur' : row[1] , 'date_publication' : row[2]}
   
for livre in bibliotheque.items():
    print(f' \n Bibliotheque initiale : {livre} \n')


csv_collecbiblio.close()



########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

#NOUVELLE BIBLIO
nouvelle_collection = open('nouvelle_collection.csv', newline ='')

d = csv.reader(nouvelle_collection)

for row_2 in d:

    titre = row_2[0]
    auteur = row_2[1]
    date_publication = row_2[2]
    new_cote = row_2[3]

    if new_cote != 'cote_rangement':
        if new_cote in bibliotheque:
            print(f"Le livre {new_cote} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque")
        
        else:
            bibliotheque[new_cote] = {'titre' : titre, 'auteur' : auteur, 'date_publication' : date_publication}
            print(f"Le livre {new_cote} ---- {titre} par {auteur} ---- a été ajouté avec succès")



########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

nouvelle_bibliotheque = bibliotheque.copy()

for row_3 in nouvelle_bibliotheque:
    if bibliotheque[row_3]['auteur'] == 'William Shakespeare':
        bibliotheque['W' + row_3] = bibliotheque.pop(row_3) 

for livre in bibliotheque.items():
    print(f' \n Bibliotheque avec modifications de cote : {livre} \n')





########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

csv_collecbiblio = open("emprunts.csv", newline='')
fichier_a_lire = csv.reader(csv_collecbiblio)

biblio_fichier_a_lire = {}

for row_3 in fichier_a_lire:
    biblio_fichier_a_lire[row_3[0]] = {'date_emprunt' : row_3[1]}


for cote in bibliotheque:

    if cote in biblio_fichier_a_lire:
        valeur = 'emprunté'
        date = biblio_fichier_a_lire[cote]['date_emprunt']
    
    else:
        valeur = 'disponible'
        date = None
    
    bibliotheque[cote].update({
        'emprunts': valeur,
        'date_emprunt': date
    })

for livre in bibliotheque.items():
    print(f'\n Bibliotheque avec ajout des emprunts : {livre} \n')




########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 


import datetime

csv_collecbiblio = open("emprunts.csv", newline='')
fichier_a_lire_date = csv.reader(csv_collecbiblio)


for cote in bibliotheque:


    if bibliotheque[cote]['emprunts'] == 'emprunté' :
        date = (datetime.date.today() - datetime.date.fromisoformat(bibliotheque[cote]['date_emprunt'])).days
        frais = 2 * (date - 30)

        if frais > 100:
            frais = 100

        if date > 365:
            bibliotheque[cote]['frais'] = frais
            bibliotheque[cote]['livre_perdus'] = 'perdus'
            

        elif date > 30:
            bibliotheque[cote]['frais'] = frais
            bibliotheque[cote]['livre_perdus'] = None
        
        else:
            frais = 0
            bibliotheque[cote]['frais'] = frais
            bibliotheque[cote]['livre_perdus'] = None 


    else:
        frais = 0
        bibliotheque[cote]['frais'] = frais
        bibliotheque[cote]['livre_perdus'] = None

for livre in bibliotheque.items():
       print(f'\n Bibliotheque avec ajout des retards et frais : {livre}\n ')

