def afficher_message():
    print("Bonjour, comment ça va ?")

afficher_message()

def afficher_nom_prenom(nom,prenom):
    print("Nom : ", nom)
    print("Prénom : ", prenom)

afficher_nom_prenom("LACOUVERTUREMEGRATTE", "Sandra")

def calculer_somme(a, b):
    resultat= a + b
    return resultat

somme = calculer_somme(2,3)
print(somme)

print("Exo chapitre")

# Définition des fonctions
def verification_saisie(saisie_utilisateur):
    if saisie_utilisateur.isnumeric() == True:
        resultat = int(saisie_utilisateur)
        return resultat
    elif "," or "." in saisie_utilisateur:
        resultat = float(saisie_utilisateur)
        return resultat

def salaire_mensuel(salaire_annuel):
    nombre_mois = 12
    resultat = salaire_annuel / nombre_mois
    return resultat

def salaire_hebdomadaire(salaire_mensuel):
    resultat = salaire_mensuel / 4.3
    return resultat

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    resultat = salaire_hebdomadaire / heures_travaillees
    resultat = round(resultat, 2)
    return resultat

salaire_annuel_utilisateur = input("Salaire annuel --> ")
print(salaire_annuel_utilisateur)
print(float(salaire_annuel_utilisateur))
heures_travaillees_utilisateur = input("Heures travaillées par semaine --> ")
print(heures_travaillees_utilisateur)

salaire_annuel = verification_saisie(salaire_annuel_utilisateur)
print(f"Votre salaire annuel est : {salaire_annuel} euros.")
heures_travaillees = verification_saisie(heures_travaillees_utilisateur)
print(f"Vous travaillez {heures_travaillees} heures par semaine.")

salaire_mensuel = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)
taux_horaire = salaire_horaire(salaire_mensuel, heures_travaillees)
print(f"Votre salaire horaire est de {taux_horaire} euros. * valeur arrondie à 2 décimales.")

# Gestion des erreurs
while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Votre saisie n'est pas valide. Veuillez saisir un nombre entier !")

