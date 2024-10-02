# CREATION PREMIERE BIBLIO
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

for livre in bibliotheque.items():
    print(f' \n Bibliotheque avec modifications de cote : {livre} \n')




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

for livre in bibliotheque.items():
    print(f'\n Bibliotheque avec ajout des emprunts : {livre} \n')



##Part 5

from datetime import datetime
csv_collecbiblio = open("emprunts.csv", newline='')
fichier_a_lire_date = csv.reader(csv_collecbiblio)

for livre in fichier_a_lire_date:

    cote = livre[0]
    if livre[1] == 'date_emprunt' and cote == 'cote_rangement':
        continue

    date_emprunt = datetime.fromisoformat(livre[1])
    date_difference = (datetime.today() - date_emprunt).days
    date_limite = date_difference - 30
        
    if date_limite > 0:
        frais = min(2 * date_limite, 100)
        bibliotheque[cote].update({'frais_retard' : frais})


    if date_difference > 365:

        bibliotheque[cote].update({'perdus' : livre[0]})
    


for livre in bibliotheque.items():
       print(f'\n Bibliotheque avec ajout des retards et frais : {livre}\n ')



