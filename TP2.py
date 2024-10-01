# CREATION PREMIERE BIBLIO
import csv

bibliotheque = {}
csv_collecbiblio = open('collection_bibliotheque.csv', newline ='')

c = csv.reader(csv_collecbiblio)

for row in c: # for cle, item in d.items():
    if row[3] == 'cote_rangement':
        continue
    bibliotheque[row[3]] = {'titre' : row[0], 'auteur' : row[1] , 'date_publication' : row[2]}
    #print(f' \n Bibliotheque initial : {bibliotheque[row[3]]} \n')



csv_collecbiblio.close()




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


###PART3:
# TODO : Écrire votre code ici
nouvelle_bibliotheque = bibliotheque.copy()

for row_3 in nouvelle_bibliotheque:
    if bibliotheque[row_3]['auteur'] == 'William Shakespeare':
        bibliotheque['W' + row_3] = bibliotheque.pop(row_3) 

#print(f' \n Bibliotheque initial : {bibliotheque} \n')






###PART 4

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



## Part 5

from datetime import datetime, timedelta, date



csv_collecbiblio = open("emprunts.csv", newline='')
fichier_a_lire_date = csv.reader(csv_collecbiblio)



today = datetime.now()
frais = {}
frais_valeur = 0
NomTitre = {}



for cote in bibliotheque: 
    if bibliotheque[cote]['date_emprunt'] != None:
        date_emprunt_valeur = datetime.fromisoformat(bibliotheque[cote]['date_emprunt']) 
        date_limite = date_emprunt_valeur + timedelta(days=30)  # Ajouter 30 jours
        jours_en_retard = (today - date_limite).days 
        date = bibliotheque[cote]['date_emprunt']
        NomTitre[cote] = {'titre' : None}

        if  jours_en_retard > 0:
            frais_valeur = min(2 * jours_en_retard, 100)
            frais[cote] = {'frais' : frais_valeur }
            NomTitre[cote] = {'titre' : None}

            if jours_en_retard > 365:
                NomTitre[cote] = {'titre' : bibliotheque[cote]['titre']}
            
            else: 
                NomTitre[cote] = {'titre' : None}
        else: 
            frais_valeur = 0
            frais[cote] = {'frais' : frais_valeur }
            NomTitre[cote] = {'titre' : None}

            

    else:
        date = None
        jours_en_retard = 0
        frais_valeur = 0
        frais[cote] = {'frais' : frais_valeur }
        NomTitre[cote] = {'titre' : None}

    bibliotheque[cote].update({'frais_retard' : frais[cote], 'liste_perdus' : NomTitre[cote] })
                         



for livre in bibliotheque.items():
    print(f'Bibliotheque initial FINAL: {livre}' )





