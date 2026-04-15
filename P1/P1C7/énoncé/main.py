campagne = {}
campagne["nom"] = "Les chiens sont les meilleurs animaux."
campagne["date_de_debut"] = "01/01/2021"
campagne["date_de_fin"] = "12/01/2031"
print(f"Notre campagne porte le nom : {campagne["nom"]} ! Elle a débuté le {campagne["date_de_debut"]} et se terminera le {campagne["date_de_fin"]}.")

print("Autre syntaxe")
nouvelle_campagne = {
    "responsable de campagne":"Jeanne d'Arc",
    "nom_de_campagne":"Campagne 'Nous aimons les chiens !'",
    "date_de_debut":"01/01/2020",
    "influenceurs_importants":["@MonAmourDeChien","@MeilleuresFriandisesPourChiens"]
}
print(nouvelle_campagne)

print("Et une autre syntaxe")
taux_de_conversion = dict()
taux_de_conversion["Facebook"] = 3.4
taux_de_conversion["Instagram"] = 1.2
print(taux_de_conversion)

print("Méthodes pour manipuler un dictionnaire")
infos_labradoodle = {
    "poids":"13 à 16 kg",
    "origine":"Etats-Unis"
}
print(infos_labradoodle)
infos_labradoodle["nom_scientifique"] = "Canis lupus familiaris"
print(infos_labradoodle)
infos_labradoodle["poids"] = "45 kg"
print(infos_labradoodle)
del infos_labradoodle["origine"]
print(infos_labradoodle)

print(infos_labradoodle.keys())
print(infos_labradoodle.values())
print(infos_labradoodle.items())
print(infos_labradoodle.get("poids"))
infos_labradoodle.pop("nom_scientifique")
print(infos_labradoodle)
print("poids" in infos_labradoodle)
infos_labradoodle.clear()
print(infos_labradoodle)
print("poids" in infos_labradoodle)

print("Exo chapitre")
fruits = {
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange"
}
print(fruits)
fruits["kiwi"] = "vert"
print(fruits)
print(fruits.get("banane"))
couleur_banane = fruits.get("banane")
fruits["pomme"] = "vert"
del fruits["banane"]
print(fruits.keys())