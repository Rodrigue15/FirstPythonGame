# Afficher un message de bienvenue
print("Bienvenue au niveau-1, Que souhaitez vous faire?")
# creer une fonction afficher parking
def afficher_parking():
    i = 1
    for place_parking in parking:
        # if place_parking == 'D':
        #     print('Parking Numero ' + str(i) + ' Disponible')
        # else:
        #     print('Parking Numero ' + str(i) + ' Indisponible')
        # utilisation de la condition terciaire
        # Nom_variable = (condition_faux, condition_vrai)[condition à verifier]
        resultat = ('Parking Numero ' + str(i) + ' Indisponible', 'Parking Numero ' + str(i) + ' Disponible')[
            place_parking == 'D']
        print(resultat)
        i += 1

parking = ['D'] * 27
afficher_parking()
# recuperer l'emplacement 3 du parking
# emplacement_selection = parking[2]
# if emplacement_selection == 'D':
#     print('Disponible')
# else:
#     print('Indisponible')

# garer une voiture au premier emplacement
parking[0] = 'V'


# proposer au client de faire une action
print("1: Garer une voiture, 2: Récuperer une voiture")
choix = int(input())
if choix == 1:
    print(" vous voulez Garer une voiture")
    print(" Choisir l'emplacement en 1 et 27")
    emplacement = int(input()) - 1
    if len(parking) > emplacement >= 0:
        if parking[emplacement] == 'D':
            print("Emplacement Disponible")
            print("Vous avez le parking Numero", emplacement + 1)
            parking[emplacement] = 'V'
        else:
            print("Emplacement Indisponible")
elif choix == 2:
    print("Recuperer une voiture")
    print(" Choisir l'emplacement en 1 et 27")
    emplacement = int(input()) - 1
    if len(parking) > emplacement >= 0:
        if parking[emplacement] == 'V':
            print("Vous pouvez recuperer votre vehicule")
            parking[emplacement] = 'D'
        else:
            print("Aucune voiture a cet emplacement")
else:
    print("Erreur choisir 1 ou 2")
afficher_parking()